from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from apps.users.models import User


class APIAuthTestMixin:

    def jwt(self):
        self.jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        self.jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        self.jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
        self.jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

    def auth(self):
        """
        User Auth
        """
        self.jwt()

        # Create and signin user
        self.test_user = User.objects.create_user(
            dni='99999000',
            username='admin',
            password='password',
            first_name='Admin',
            last_name='Nacional',
            is_superuser=True
        )

        user = authenticate(username='admin', password='password')
        payload = self.jwt_payload_handler(user)

        self.user_session = {
            'token': self.jwt_encode_handler(payload),
            'user': user
        }

    def auth_login(self, login):
        """
        User Auth custom role
        """
        self.jwt()
        user = authenticate(username=login['username'], password=login['password'])
        payload = self.jwt_payload_handler(user)

        self.user_session = {
            'token': self.jwt_encode_handler(payload),
            'user': user
        }
