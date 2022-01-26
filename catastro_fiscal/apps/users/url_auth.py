from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = 'api_auth'

urlpatterns = [
    path('sign-in/', obtain_jwt_token),
    path('verify-access-token/', verify_jwt_token),
    path('refresh-access-token/', refresh_jwt_token)
]
