import uuid
from django.core.cache import caches
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_captcha.settings import api_settings
from rest_captcha import utils, captcha
from ..models import User

cache = caches[api_settings.CAPTCHA_CACHE]


class ApiSignInTest(APITestCase):
    """
    Unit tests to validate api post `api:api_auth:sign-in`
    """
    fixtures = ["master.json"]

    def setUp(self):
        """
        User Data for test
        """
        self.test_user = User.objects.create_user(
            dni='99999001',
            username='99999001',
            password='prueba',
            first_name='Usuario',
            last_name='Nacional',
        )

        self.url_api = reverse('api:api_auth:sign-in')

    def make_captcha(self):
        """
        method used for generate captcha key and captcha value
        """
        key = str(uuid.uuid4())
        value = utils.random_char_challenge(api_settings.CAPTCHA_LENGTH)
        cache_key = utils.get_cache_key(key)
        cache.set(cache_key, value, api_settings.CAPTCHA_TIMEOUT)
        return value, key

    def test_api_sign_in_valid(self):
        """
        test api sign-in if data is valid
        """
        captcha_value, captcha_key = self.make_captcha()

        data = {
            'username': '99999001',
            'password': 'prueba',
            'captcha_value': captcha_value,
            'captcha_key': captcha_key

        }
        response = self.client.post(self.url_api, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_sign_in_without_captcha(self):
        """
        test api sign-in if data without captcha
        """
        data = {
            'username': '99999001',
            'password': 'prueba'
        }
        response = self.client.post(self.url_api, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_sign_in_with_password_error(self):
        """
        test api sign-in if data has password error
        """
        captcha_value, captcha_key = self.make_captcha()
        data = {
            'username': '99999001',
            'password': 'error_password',
            'captcha_value': captcha_value,
            'captcha_key': captcha_key

        }
        response = self.client.post(self.url_api, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
