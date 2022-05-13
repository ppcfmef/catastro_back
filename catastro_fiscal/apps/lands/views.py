from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from core.views import CustomSerializerMixin
from .models import UploadHistory, Land, LandOwner
from .serializers import UploadHistorySerializer, UploadHistoryListSerializer, LandSerializer, LandOwnerSerializer


class UploadHistoryViewset(CustomSerializerMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = UploadHistory.objects.all()
    serializer_class = UploadHistoryListSerializer
    create_serializer_class = UploadHistorySerializer
    parser_classes = (CamelCaseMultiPartParser, )

    @swagger_auto_schema(request_body=UploadHistorySerializer)
    def create(self, request, *args, **kwargs):
        return super(UploadHistoryViewset, self).create(request, *args, **kwargs)


class LandViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['habilitacion_name', 'steet_name', ]
    filterset_fields = ['owner', ]


class LandOwnerViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['dni', 'name', 'paternal_surname', 'maternal_surname', ]
    filterset_fields = ['id', ]
