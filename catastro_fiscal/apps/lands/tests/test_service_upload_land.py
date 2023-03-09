import random
from django.test import TestCase
from apps.lands.models import Land, LandOwner
from ..services.upload_temporal import UploadTemporalService
from ..services.upload_land import UploadLandService
from .upload_setup_test_data import UploadSetUpTestData


class UploadLandTest(TestCase):
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
        UploadTemporalService().execute(upload_history=UploadSetUpTestData.get_upload_history())

    def test_land_owner_upload(self):
        """
        test for method `UploadTemporalService.land_owner_upload` validate the number of land owners created
        """
        upload_history = UploadSetUpTestData.get_upload_history()
        UploadLandService().land_owner_upload(upload_history)
        self.assertEquals(LandOwner.objects.count(), UploadSetUpTestData.UPLOAD_FILE_LAND_OWNERS)

    def test_land_upload(self):
        """
        test for method `UploadTemporalService.land_upload` validate the number of lands created
        """
        upload_history = UploadSetUpTestData.get_upload_history()
        UploadLandService().land_owner_upload(upload_history)
        UploadLandService().land_upload(upload_history)
        self.assertEquals(Land.objects.count(), UploadSetUpTestData.UPLOAD_FILE_LANDS)

    def test_count_lands_by_owner(self):
        """
        test for method `UploadTemporalService.count_lands_by_owner` validate the number of lands by Owner
        """
        upload_history = UploadSetUpTestData.get_upload_history()
        UploadLandService().land_owner_upload(upload_history)
        UploadLandService().land_upload(upload_history)
        UploadLandService().count_lands_by_owner()
        land_owner = LandOwner.objects.get(dni=UploadSetUpTestData.UPLOAD_FILE_DOCUMENTS[0])
        lands_by_owner = Land.objects.filter(owner_id=land_owner.pk)
        self.assertEquals(land_owner.number_lands, lands_by_owner.count())
