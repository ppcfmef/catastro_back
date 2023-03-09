import json
from rest_framework.reverse import reverse
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings
from ..models import User
from .user_setup_test_data import UserSetUpTestData

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class ApiUserTest(APITestCase):
    """
    Unit tests to validate api `api:api_user:users` for all methods
    """
    fixtures = ["master.json"]

    def setUp(self):
        """
        User Data for test
        """

        # Create and signin user
        self.test_user = User.objects.create_user(
            dni='99999000',
            username='99999000',
            password='password',
            first_name='Usuario',
            last_name='Nacional',
        )

        user = authenticate(username='99999000', password='password')
        payload = jwt_payload_handler(user)

        self.user_session = {
            'token': jwt_encode_handler(payload),
            'user': user
        }

        # create other users
        UserSetUpTestData.mock()

    def test_user_list(self):
        """
        test api user method api list `api:api_user:users-list` validate api valid and count data return
        """
        api_url = reverse('api:api_user:users-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.get(api_url, format='json')
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['count'],  User.objects.count())
