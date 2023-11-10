from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    MobileObtainJSONWebToken, MobileVerifyJSONWebToken, MobileRefreshJSONWebToken, MobileUserProfileShortView,
    LandInspectionViewset
)

app_name = 'api_mobile'

router = DefaultRouter()
router.register(r'land-inspection', LandInspectionViewset)

urlpatterns = [
    path('auth/sign-in/', MobileObtainJSONWebToken.as_view(), name='sign-in'),
    path('auth/verify-access-token/', MobileVerifyJSONWebToken.as_view(), name='verify-token'),
    path('auth/refresh-access-token/', MobileRefreshJSONWebToken.as_view(), name='refresh-token'),
    path('users/user/', MobileUserProfileShortView.as_view(), name='user_profile'),
] + router.urls

