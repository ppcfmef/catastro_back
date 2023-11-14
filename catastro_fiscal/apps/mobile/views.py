from rest_framework import viewsets, mixins, status, exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from apps.users.views import UserProfileShortView
from apps.land_inspections.models import LandInspectionUpload
from apps.land_inspections.serializers import MobileLandInspectionSerializer
from .serializers import MobileJWTSerializer, GeneralResponseSerializer
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


class LandInspectionViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = LandInspectionUpload.objects.all()
    serializer_class = MobileLandInspectionSerializer
    response_serializer_class = GeneralResponseSerializer
    permission_classes = [HasAPIKey & IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
            response_serializer = self.response_serializer_class({
                "status": "success",
                "message": "El registro se guardo correctamente"
            })
        except:
            response_serializer = self.response_serializer_class({
                "status": "error",
                "message": "Error al guardar registros"
            })
            raise exceptions.ValidationError(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
