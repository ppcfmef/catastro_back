import os
import shutil
import random
from django.conf import settings
from django.test import TestCase
from apps.lands.models import UploadHistory, TemploralUploadRecord
from ..services.upload_temporal import UploadTemporalService


class UploadSetUpTestData:
    UPLOAD_HISTORY_TEST_ID = 1
    UPLOAD_FILENAME = 'predios_test_v6.6.xlsx'
    UPLOAD_FILE_RECORDS = 10
    UPLOAD_FILE_UBIGEO = '040703'
    UPLOAD_FILE_DOCUMENTS = ['30846549', '30825501', '01544376', '30847064', '30847078', '30847063', '30846530',
                             '30847071', '040703-1', '30850106']

    @staticmethod
    def upload_history():
        fixture_upload_file = settings.FIXTURE_DIRS[0] / 'test' / UploadSetUpTestData.UPLOAD_FILENAME
        media_upload_file = settings.MEDIA_ROOT / 'test' / UploadSetUpTestData.UPLOAD_FILENAME
        if not media_upload_file.is_file():
            os.makedirs(str(media_upload_file.parent), exist_ok=True)
            shutil.copyfile(str(fixture_upload_file), str(media_upload_file))

        UploadHistory.objects.create(
            id=UploadSetUpTestData.UPLOAD_HISTORY_TEST_ID,
            file_upload='test/predios_test_v6.6.xlsx'
        )


class UploadTemporalTest(TestCase):
    """
    Unit tests to upload land
    """
    fixtures = ["master.json"]

    @classmethod
    def setUpTestData(cls):
        """
        User Data for all test
        """
        UploadSetUpTestData.upload_history()

    def _get_upload_history(self):
        """
        Get a UploadHistory object for test using UPLOAD_HISTORY_TEST_ID
        :return: UploadHistory
        """
        return UploadHistory.objects.get(id=UploadSetUpTestData.UPLOAD_HISTORY_TEST_ID)

    def test_read_records(self):
        """
        test for method `UploadTemporalService.read` validate count records, this test also validates the excel
        reading class `ReadXlsxService`
        """
        upload_history = self._get_upload_history()
        file_records_read = UploadTemporalService().read(upload_history)
        self.assertEquals(len(file_records_read), UploadSetUpTestData.UPLOAD_FILE_RECORDS)

    def test_update_ubigeo(self):
        """
        test for method `UploadTemporalService.update_ubigeo` validate update ubigeo in `UploadHistory.ubigeo`
        """
        upload_history = self._get_upload_history()
        file_records_read = UploadTemporalService().read(upload_history)
        UploadTemporalService().update_ubigeo(upload_history, records=file_records_read)
        upload_history_update = self._get_upload_history()
        self.assertEquals(upload_history_update.ubigeo_id, UploadSetUpTestData.UPLOAD_FILE_UBIGEO)

    def test_make_document(self):
        """
        test for method `UploadTemporalService.make_document` validate the document key create for record
        """
        upload_history = self._get_upload_history()
        upload_service = UploadTemporalService()
        file_records_read = upload_service.read(upload_history)
        documents = [upload_service.make_document(record) for record in file_records_read]
        self.assertEquals(documents, UploadSetUpTestData.UPLOAD_FILE_DOCUMENTS)

    def test_upload_temporal_ramdom_records(self):
        """
        test for method `UploadTemporalService.temporal_upload` validates the main functionality using random records
        """
        upload_history = self._get_upload_history()
        file_records_read = UploadTemporalService().read(upload_history)
        random_number = random.randint(1, UploadSetUpTestData.UPLOAD_FILE_RECORDS)
        random_records = random.choices(file_records_read, k=random_number)
        UploadTemporalService().temporal_upload(upload_history, records=random_records)
        upload_records = TemploralUploadRecord.objects.filter(upload_history_id=upload_history.pk)
        self.assertEquals(upload_records.count(), random_number)

    def test_upload_temporal_summary(self):
        upload_history = self._get_upload_history()
        UploadTemporalService().execute(upload_history)
        upload_history_update = self._get_upload_history()
        temporal_summary = UploadTemporalService().get_temporal_summary(upload_history=upload_history_update)
        upload_records_corrects = TemploralUploadRecord.objects.filter(upload_history_id=upload_history.pk,
                                                                       status__in=['OK_NEW', 'OK_OLD'])
        self.assertEquals(temporal_summary['corrects'], upload_records_corrects.count())
