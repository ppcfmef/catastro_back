from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import CamelCaseOrderFilter
from core.views import CustomSerializerMixin
from .models import UploadHistory, Land, LandOwner, LandOwnerDetail
from .serializers import (
    UploadHistorySerializer, UploadHistoryListSerializer, LandSerializer, LandOwnerSerializer,
    LandOwnerDetailSerializer, LandOwnerSaveSerializer, LandDetailSerializer, LandSaveSerializer,
    SummaryRecordSerializer, TemporalUploadSummarySerializer, UploadStatusSerializer
)
from .services.upload_temporal import UploadTemporalService
from apps.historical.models import HistoricalRecord
from .filters import LandOwnerFilter


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


    def perform_update(self, serializer):
        user = self.request.user
        serializer.save()
        HistoricalRecord.register(
            user,
            serializer.instance,
            type_event=HistoricalRecord.RecordEvent.CREATED,
            event="Carga masiva",
            module="Gestor de predios - Carga de datos",
        )

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
    filterset_fields = ['owner', 'status', 'id', 'ubigeo']
    ordering_fields = ['ubigeo', 'cup', 'cpm', 'id_plot', 'id_cartographic_img', 'habilitacion_name', 'street_name',
                       'creation_date']
    ordering = ['-creation_date']

    @action(methods=['GET'], detail=False, url_path='by-owner/(?P<owner_id>[0-9]+)')
    def record_by_owner(self, request, *args, **kwargs):
        owner_id = kwargs.get('owner_id')
        ubigeo = request.query_params.get('ubigeo')
        qs_detail = LandOwnerDetail.objects.filter(owner_id=owner_id)
        if ubigeo:
            qs_detail = qs_detail.filter(ubigeo=ubigeo)

        lands_id = qs_detail.values_list('land_id', flat=True)
        lands = self.get_queryset().filter(id__in=list(lands_id))
        queryset = self.filter_queryset(lands)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save()
        HistoricalRecord.register(user, serializer.instance, type_event=HistoricalRecord.RecordEvent.CREATED)

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save()
        HistoricalRecord.register(user, serializer.instance, type_event=HistoricalRecord.RecordEvent.UPDATED)


class LandOwnerViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSerializer
    filter_class = LandOwnerFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    search_fields = ['dni', 'name', 'paternal_surname', 'maternal_surname', ]
    #filterset_fields = ['id', 'dni','ubigeo' ]
    ordering_fields = ['document_type', 'dni', 'name', 'paternal_surname', 'maternal_surname', 'creation_date']
    ordering = ['-creation_date']

    @action(methods=['GET'], detail=False, url_path='by-land/(?P<land_id>[0-9]+)')
    def owners_by_land(self, request, *args, **kwargs):
        land_id = kwargs.get('land_id')
        owners_id = LandOwnerDetail.objects.filter(land_id=land_id).values_list('owner_id', flat=True)
        owners = self.get_queryset().filter(id__in=list(owners_id))
        queryset = self.filter_queryset(owners)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LandOwnerDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    Get Owner filter by id
    """
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerDetailSerializer


class OwnerSearchByDocumentViewset(mixins.ListModelMixin, GenericViewSet):
    """
    Get Owner filter by document (dni, ruc)
    """
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerDetailSerializer
    #lookup_field = 'dni'
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['dni', 'ubigeo','code' ]
    search_fields = ['code','=dni']
    pagination_class = None
    

class CreateAndEditOwnerViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSaveSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save()
        HistoricalRecord.register(user, serializer.instance, type_event=HistoricalRecord.RecordEvent.CREATED)

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save()
        HistoricalRecord.register(user, serializer.instance, type_event=HistoricalRecord.RecordEvent.UPDATED)


class SearchInactiveLandByCpu(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Land.objects.filter(status=3)
    serializer_class = LandDetailSerializer
    lookup_field = 'cup'


class SummaryRecord(GenericAPIView):
    queryset = Land.objects.exclude(status=3)
    serializer_class = SummaryRecordSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['ubigeo']

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        summary = self.get_summary(queryset)
        serializer = self.serializer_class(summary, context={"request": request})
        return Response(serializer.data)

    def get_summary(self, queryset):
        total_records = queryset.count()
        without_mapping_records = queryset.filter(status=0).count()
        mapping_records = total_records - without_mapping_records
        return {
            'total_records': total_records,
            'mapping_records': mapping_records,
            'without_mapping_records': without_mapping_records
        }
