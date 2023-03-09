from django.test import TestCase
from ..models import User
from .user_setup_test_data import UserSetUpTestData


class UserModelScopeTest(TestCase):
    """
    Unit tests to validate the scope of a new registered user
    """
    fixtures = ["master.json"]

    @classmethod
    def setUpTestData(cls):
        """
        User Data for all test
        """
        UserSetUpTestData.mock()

    def test_national_scope(self):
        test_user_national = User.objects.get(username='99999001')
        self.assertEquals(test_user_national.place_scope_id, UserSetUpTestData.NATIONAL_SCOPE)

    def test_department_scope(self):
        test_user_department = User.objects.get(username='99999002')
        self.assertEquals(test_user_department.place_scope_id, UserSetUpTestData.DEPARTMENT_SCOPE)

    def test_province_scope(self):
        test_user_province = User.objects.get(username='99999003')
        self.assertEquals(test_user_province.place_scope_id, UserSetUpTestData.PROVINCE_SCOPE)

    def test_district_scope(self):
        test_user_district = User.objects.get(username='99999004')
        self.assertEquals(test_user_district.place_scope_id, UserSetUpTestData.DISTRICT_SCOPE)


class UserModelUbigeoTest(TestCase):
    """
    Unit tests to validate ubigeo of a new registered user
    """
    fixtures = ["master.json"]

    @classmethod
    def setUpTestData(cls):
        """
        User Data for all test
        """
        UserSetUpTestData.mock()

    def test_national_ubigeo(self):
        test_user_national = User.objects.get(username='99999001')
        self.assertIsNone(test_user_national.ubigeo)

    def test_department_ubigeo(self):
        test_user_department = User.objects.get(username='99999002')
        self.assertEquals(test_user_department.ubigeo, '15')

    def test_province_ubigeo(self):
        test_user_province = User.objects.get(username='99999003')
        self.assertEquals(test_user_province.ubigeo, '1501')

    def test_district_ubigeo(self):
        test_user_district = User.objects.get(username='99999004')
        self.assertEquals(test_user_district.ubigeo, '150101')
