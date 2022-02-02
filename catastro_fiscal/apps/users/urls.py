from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfileShortView, UserViewSet

app_name = 'api_user'

router = DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = [
    path('user/', UserProfileShortView.as_view())
] + router.urls
