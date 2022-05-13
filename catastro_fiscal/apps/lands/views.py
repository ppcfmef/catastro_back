from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from drf_yasg.utils import swagger_auto_schema
from core.views import CustomSerializerMixin
from .models import UploadHistory
from .serializers import UploadHistorySerializer, UploadHistoryListSerializer


class UploadHistoryViewset(CustomSerializerMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = UploadHistory.objects.all()
    serializer_class = UploadHistoryListSerializer
    create_serializer_class = UploadHistorySerializer
    parser_classes = (CamelCaseMultiPartParser, )

    @swagger_auto_schema(request_body=UploadHistorySerializer)
    def create(self, request, *args, **kwargs):
        return super(UploadHistoryViewset, self).create(request, *args, **kwargs)
