from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from apps.users.views import UserProfileShortView
from .serializers import MobileJWTSerializer
from .api_key_permissions import CustomHasAPIKey as HasAPIKey


class HasAPIKeyPermissionMixin:
    permission_classes = [HasAPIKey]


class MobileObtainJSONWebToken(HasAPIKeyPermissionMixin, ObtainJSONWebToken):
    serializer_class = MobileJWTSerializer


class MobileRefreshJSONWebToken(HasAPIKeyPermissionMixin, RefreshJSONWebToken):
    pass


class MobileVerifyJSONWebToken(HasAPIKeyPermissionMixin, VerifyJSONWebToken):
    pass


class MobileUserProfileShortView(UserProfileShortView):
    permission_classes = [HasAPIKey & IsAuthenticated]
