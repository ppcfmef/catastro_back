from django.urls import path
from .views import MobileObtainJSONWebToken, MobileVerifyJSONWebToken, MobileRefreshJSONWebToken

app_name = 'api_mobile'


urlpatterns = [
    path('auth/sign-in/', MobileObtainJSONWebToken.as_view(), name='sign-in'),
    path('auth/verify-access-token/', MobileVerifyJSONWebToken.as_view(), name='verify-token'),
    path('auth/refresh-access-token/', MobileRefreshJSONWebToken.as_view(), name='refresh-token')
]
