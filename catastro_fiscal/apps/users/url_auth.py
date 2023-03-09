from django.urls import path
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_captcha.serializers import RestCaptchaSerializer


app_name = 'api_auth'


class MyJWTSerializer(JSONWebTokenSerializer, RestCaptchaSerializer):
    def validate(self, data):
        response = RestCaptchaSerializer.validate(self, data)
        if response:
            return JSONWebTokenSerializer.validate(self, data)
        else:
            return response


obtain_jwt_token_1 = ObtainJSONWebToken.as_view(
    serializer_class=MyJWTSerializer
)


urlpatterns = [
    path('sign-in/', obtain_jwt_token_1, name='sign-in'),
    path('verify-access-token/', verify_jwt_token, name='verify-token'),
    path('refresh-access-token/', refresh_jwt_token, name='refresh-token')
]
