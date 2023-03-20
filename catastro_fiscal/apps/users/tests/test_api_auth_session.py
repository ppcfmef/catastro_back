from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .api_auth_test_mixin import APIAuthTestMixin


class ApiAuthSessionTest(APIAuthTestMixin, APITestCase):
    """
    Unit tests to validate api auth
    """
    fixtures = ["master.json"]

    def setUp(self):
        """
        Auth setup for test
        """

        self.auth()

    def test_api_verify_token(self):
        """
        test api user method api list `api:api_user:users-list` validate api exists and valid
        """
        api_url = reverse('api:api_auth:verify-token')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.post(api_url, {'token': self.user_session['token']}, format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user_session['token'], response_data['token'])

    def test_api_refresh_token(self):
        """
        test api auth method api list `api:api_auth:refresh-token` validate api exists and valid
        """
        api_url = reverse('api:api_auth:refresh-token')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_session['token']}")
        response = self.client.post(api_url, {'token': self.user_session['token']}, format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNot(self.user_session['token'], response_data['token'])
