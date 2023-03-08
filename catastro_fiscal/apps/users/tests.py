from django.test import TestCase
from .models import *

NATIONAL_SCOPE = 1
DEPARTMENT_SCOPE = 2
PROVINCE_SCOPE = 3
DISTRICT_SCOPE = 4


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
        User.objects.create_user(
            dni='99999001',
            username='99999001',
            password='prueba',
            first_name='Usuario',
            last_name='Nacional',
        )

        User.objects.create_user(
            dni='99999002',
            username='99999002',
            password='prueba',
            first_name='Usuario',
            last_name='Departamental',
            department_id='15',
        )

        User.objects.create_user(
            dni='99999003',
            username='99999003',
            password='prueba',
            first_name='Usuario',
            last_name='Distrital',
            department_id='15',
            province_id='1501'
        )

        User.objects.create_user(
            dni='99999004',
            username='99999004',
            password='prueba',
            first_name='Usuario',
            last_name='Distrital',
            department_id='15',
            province_id='1501',
            district_id='150101'
        )

    def test_national_scope(self):
        test_user_national = User.objects.get(username='99999001')
        self.assertEquals(test_user_national.place_scope_id, NATIONAL_SCOPE)

    def test_department_scope(self):
        test_user_department = User.objects.get(username='99999002')
        self.assertEquals(test_user_department.place_scope_id, DEPARTMENT_SCOPE)

    def test_province_scope(self):
        test_user_province = User.objects.get(username='99999003')
        self.assertEquals(test_user_province.place_scope_id, PROVINCE_SCOPE)

    def test_district_scope(self):
        test_user_district = User.objects.get(username='99999004')
        self.assertEquals(test_user_district.place_scope_id, DISTRICT_SCOPE)


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
        User.objects.create_user(
            dni='99999001',
            username='99999001',
            password='prueba',
            first_name='Usuario',
            last_name='Nacional',
        )

        User.objects.create_user(
            dni='99999002',
            username='99999002',
            password='prueba',
            first_name='Usuario',
            last_name='Departamental',
            department_id='15',
        )

        User.objects.create_user(
            dni='99999003',
            username='99999003',
            password='prueba',
            first_name='Usuario',
            last_name='Distrital',
            department_id='15',
            province_id='1501'
        )

        User.objects.create_user(
            dni='99999004',
            username='99999004',
            password='prueba',
            first_name='Usuario',
            last_name='Distrital',
            department_id='15',
            province_id='1501',
            district_id='150101'
        )

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
