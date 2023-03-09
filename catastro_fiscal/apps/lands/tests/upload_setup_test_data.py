import os
import shutil
from django.conf import settings
from apps.lands.models import UploadHistory


class UploadSetUpTestData:
    UPLOAD_HISTORY_TEST_ID = 1
    UPLOAD_FILENAME = 'predios_test_v6.6.xlsx'
    UPLOAD_FILE_RECORDS = 10
    UPLOAD_FILE_LAND_OWNERS = 10
    UPLOAD_FILE_LANDS = 9
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

    @staticmethod
    def get_upload_history():
        """
        Get a UploadHistory object for test using UPLOAD_HISTORY_TEST_ID
        :return: UploadHistory
        """
        return UploadHistory.objects.get(id=UploadSetUpTestData.UPLOAD_HISTORY_TEST_ID)
