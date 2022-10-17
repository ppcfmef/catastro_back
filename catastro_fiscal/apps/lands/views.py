from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from core.views import CustomSerializerMixin
from .models import UploadHistory, Land, LandOwner
from .serializers import (
    UploadHistorySerializer, UploadHistoryListSerializer, LandSerializer, LandOwnerSerializer,
    LandOwnerDetailSerializer, LandOwnerSaveSerializer, LandDetailSerializer, LandSaveSerializer,
    SummaryRecordSerializer, TemporalUploadSummarySerializer
)


class UploadHistoryViewset(CustomSerializerMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = UploadHistory.objects.all()
    serializer_class = UploadHistoryListSerializer
    create_serializer_class = UploadHistorySerializer
    parser_classes = (CamelCaseMultiPartParser, )

    """
    @swagger_auto_schema(request_body=UploadHistorySerializer)
    def create(self, request, *args, **kwargs):
        return super(UploadHistoryViewset, self).create(request, *args, **kwargs)
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        a = serializer.save()
        serializer_response = TemporalUploadSummarySerializer(a)
        return Response(serializer_response.data, status=status.HTTP_201_CREATED)


class LandViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['cup', 'cpm', 'id_cartographic_img', 'id_plot', 'street_name']
    filterset_fields = ['owner', ]


class LandDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Land.objects.all()
    serializer_class = LandDetailSerializer


class LandCreateAndEditViewset(mixins.CreateModelMixin,
                               mixins.UpdateModelMixin,  # ToDo: only patch
                               GenericViewSet):
    """
    Create and Update Land Record
    """
    queryset = Land.objects.all()
    serializer_class = LandSaveSerializer


class LandOwnerViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['dni', 'name', 'paternal_surname', 'maternal_surname', ]
    filterset_fields = ['id', ]


class OwnerSearchByDocumentViewset(mixins.RetrieveModelMixin, GenericViewSet):
    """
    Get Owner filter by document (dni, ruc)
    """
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerDetailSerializer
    lookup_field = 'dni'


class CreateAndEditOwnerViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSaveSerializer


class SearchInactiveLandByCpu(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Land.objects.filter(status=3)
    serializer_class = LandDetailSerializer
    lookup_field = 'cup'


class SummaryRecord(APIView):
    queryset = Land.objects.exclude(status=3)
    serializer_class = SummaryRecordSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"request": request})
        return Response(serializer.data)

    def get_object(self):
        total_records = self.queryset.count()
        mapping_records = self.queryset.filter(longitude__isnull=False, latitude__isnull=False).count()
        without_mapping_records = total_records - mapping_records
        return {
            'total_records': total_records,
            'mapping_records': mapping_records,
            'without_mapping_records': without_mapping_records
        }
