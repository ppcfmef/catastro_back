from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from rest_framework_api_key.permissions import HasAPIKey
from .serializers import MobileJWTSerializer


class HasAPIKeyPermissionMixin:
    permission_classes = [HasAPIKey]


class MobileObtainJSONWebToken(HasAPIKeyPermissionMixin, ObtainJSONWebToken):
    serializer_class = MobileJWTSerializer


class MobileRefreshJSONWebToken(HasAPIKeyPermissionMixin, RefreshJSONWebToken):
    pass


class MobileVerifyJSONWebToken(HasAPIKeyPermissionMixin, VerifyJSONWebToken):
    pass
