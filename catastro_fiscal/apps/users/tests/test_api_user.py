import json
from rest_framework.reverse import reverse
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings
from core.tests.api_auth_test_mixin import APIAuthTestMixin
from ..models import User, Role
from .user_setup_test_data import UserSetUpTestData

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class ApiUserTest(APIAuthTestMixin, APITestCase):
    """
    Unit tests to validate api `api:api_user:users` for all methods
    """
    fixtures = ["master.json"]

    def setUp(self):
        """
        User Data for test
        """

        self.auth()

    def test_user_list(self):
        """
        test api user method api list `api:api_user:users-list` validate api valid and count data return
        """
        # create other users
        UserSetUpTestData.mock()

        api_url = reverse('api:api_user:users-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['count'],  User.objects.exclude(is_superuser=True).count())

    def test_user_register(self):
        """
        test api user method api user validate new user is register
        """
        role = Role.objects.create(name='Demo', description='Demo Role')
        # new User
        new_user = {
            'dni': '99999001', 'first_name': 'Demo', 'last_name': 'New', 'email': 'demo@newuser.com',
            'role': role.id, 'username': '99999001', 'password': 'password', 'department': '15',
            'province': '1501', 'district': '150101'
        }

        api_url = reverse('api:api_user:users-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.post(api_url, new_user, format='json')
        response_data = response.json()
        user = User.objects.get(username=new_user['username'])
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response_data['id'], user.id)

    def test_user_change(self):
        """
        test api user method api user validate other fields change
        """
        new_user = {
            'dni': '99999001', 'first_name': 'Demo', 'last_name': 'New', 'email': 'demo@newuser.com',
            'username': '99999001', 'password': 'password', 'department_id': '15', 'province_id': '1501',
            'district_id': '150101'
        }

        new_user = User.objects.create(**new_user)

        api_url = reverse('api:api_user:users-detail', str(new_user.pk))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        data = {'first_name': 'Otro Nombre', 'last_name': 'Otro Apellido'}
        response = self.client.patch(api_url, data, format='json')
        user = User.objects.get(pk=new_user.pk)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(user.get_full_name(), f'Otro Nombre Otro Apellido')

    def test_user_change_password(self):
        """
        test api user method api user validate password change
        """
        new_user = {
            'dni': '99999001', 'first_name': 'Demo', 'last_name': 'New', 'email': 'demo@newuser.com',
            'username': '99999001', 'password': 'password', 'department_id': '15', 'province_id': '1501',
            'district_id': '150101'
        }

        new_user = User.objects.create(**new_user)
    
        api_url = reverse('api:api_user:users-detail', str(new_user.pk))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.patch(api_url, {'password': '123456'}, format='json')
        response_data = response.json()
        user = User.objects.get(pk=new_user.pk)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['id'], new_user.pk)
        self.assertEquals(user.check_password('123456'), True)

    def test_user_username_not_change(self):
        """
        test api user method api user validate username not change
        """
        new_user = {
            'dni': '99999001', 'first_name': 'Demo', 'last_name': 'New', 'email': 'demo@newuser.com',
            'username': '99999001', 'password': 'password', 'department_id': '15', 'province_id': '1501',
            'district_id': '150101'
        }

        new_user = User.objects.create(**new_user)

        api_url = reverse('api:api_user:users-detail', str(new_user.pk))
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.patch(api_url, {'username': 'changeusername'}, format='json')
        user = User.objects.get(pk=new_user.pk)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(user.username, new_user.username)
