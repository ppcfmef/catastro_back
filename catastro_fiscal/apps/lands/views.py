from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import CamelCaseOrderFilter
from core.views import CustomSerializerMixin
from .models import UploadHistory, Land, LandOwner
from .serializers import (
    UploadHistorySerializer, UploadHistoryListSerializer, LandSerializer, LandOwnerSerializer,
    LandOwnerDetailSerializer, LandOwnerSaveSerializer, LandDetailSerializer, LandSaveSerializer,
    SummaryRecordSerializer, TemporalUploadSummarySerializer, UploadStatusSerializer, LandHistorySerializer
)
from .services.upload_temporal import UploadTemporalService


class UploadHistoryViewset(CustomSerializerMixin, mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = UploadHistory.objects.all().order_by('-id')
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


class UploadStatusViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = UploadHistory.objects.all()
    serializer_class = UploadStatusSerializer


class UploadHistorySummaryViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = UploadHistory.objects.all()
    serializer_class = UploadHistoryListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        upload_sumary = UploadTemporalService().get_temporal_summary(upload_history=instance)
        serializer_response = TemporalUploadSummarySerializer(upload_sumary)
        return Response(serializer_response.data, status=status.HTTP_201_CREATED)


class LandViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    search_fields = ['cup', 'cpm', 'id_cartographic_img', 'id_plot', 'street_name']
    filterset_fields = ['owner', 'status', 'id']
    ordering_fields = ['ubigeo', 'cup', 'cpm', 'id_plot', 'id_cartographic_img', 'habilitacion_name', 'street_name',
                       'creation_date']
    ordering = ['-creation_date']

    @action(detail=False, methods=['get'])
    def history_detail(self, request, *args, **kwargs):
        username = request.GET.get("username") or request.GET.get("search")
        queryset = Land.objects.filter(created_by=username).order_by('-update_date')
        serializer_response = LandHistorySerializer(queryset, many=True)
        return Response(serializer_response.data)


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
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    search_fields = ['dni', 'name', 'paternal_surname', 'maternal_surname', ]
    filterset_fields = ['id', ]
    ordering_fields = ['document_type', 'dni', 'name', 'paternal_surname', 'maternal_surname', 'creation_date']
    ordering = ['-creation_date']


class LandOwnerDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    Get Owner filter by id
    """
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerDetailSerializer


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
