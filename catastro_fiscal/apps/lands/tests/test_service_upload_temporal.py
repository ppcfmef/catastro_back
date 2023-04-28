import random
from django.test import TestCase
from apps.lands.models import TemploralUploadRecord
from ..services.upload_temporal import UploadTemporalService
from .upload_setup_test_data import UploadSetUpTestData


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

    def test_read_records(self):
        """
        test for method `UploadTemporalService.read` validate count records, this test also validates the excel
        reading class `ReadXlsxService`
        """
        upload_history = UploadSetUpTestData.get_upload_history()
        file_records_read = UploadTemporalService().read(upload_history)
        self.assertEquals(len(file_records_read), UploadSetUpTestData.UPLOAD_FILE_RECORDS)

    def test_update_ubigeo(self):
        """
        test for method `UploadTemporalService.update_ubigeo` validate update ubigeo in `UploadHistory.ubigeo`
        """
        upload_history = UploadSetUpTestData.get_upload_history()
        file_records_read = UploadTemporalService().read(upload_history)
        UploadTemporalService().update_ubigeo(upload_history, records=file_records_read)
        upload_history_update = UploadSetUpTestData.get_upload_history()
        self.assertEquals(upload_history_update.ubigeo_id, UploadSetUpTestData.UPLOAD_FILE_UBIGEO)

    def test_upload_temporal_ramdom_records(self):
        """
        test for method `UploadTemporalService.temporal_upload` validates the main functionality using random records
        """
        upload_history = UploadSetUpTestData.get_upload_history()
        file_records_read = UploadTemporalService().read(upload_history)
        random_number = random.randint(1, UploadSetUpTestData.UPLOAD_FILE_RECORDS)
        random_records = random.choices(file_records_read, k=random_number)
        UploadTemporalService().temporal_upload(upload_history, records=random_records)
        upload_records = TemploralUploadRecord.objects.filter(upload_history_id=upload_history.pk)
        self.assertEquals(upload_records.count(), random_number)

    def test_upload_temporal_summary(self):
        upload_history = UploadSetUpTestData.get_upload_history()
        UploadTemporalService().execute(upload_history)
        upload_history_update = UploadSetUpTestData.get_upload_history()
        temporal_summary = UploadTemporalService().get_temporal_summary(upload_history=upload_history_update)
        upload_records_corrects = TemploralUploadRecord.objects.filter(upload_history_id=upload_history.pk,
                                                                       status__in=['OK_NEW', 'OK_OLD'])
        self.assertEquals(temporal_summary['corrects'], upload_records_corrects.count())
