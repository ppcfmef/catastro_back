from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileShortView, UserViewSet, RoleViewSet, RoleSelectViewSet, PermissionViewSet, PermissionTypeViewSet
)

app_name = 'api_user'

router = DefaultRouter()

router.register(r'role/select', RoleSelectViewSet)
router.register(r'role', RoleViewSet)
router.register(r'permission/type', PermissionTypeViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'', UserViewSet)

urlpatterns = [
    path('user/', UserProfileShortView.as_view())
] + router.urls
