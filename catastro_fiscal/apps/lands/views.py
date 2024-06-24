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
    SummaryRecordSerializer, TemporalUploadSummarySerializer, UploadStatusSerializer,LandOwnerSRTMSerializer,LandOwnerDetailSRTMSerializer, OwnerDeudaSerializer,LandNivelConstruccionSerializer
)
from .services.upload_temporal import UploadTemporalService
from apps.historical.models import HistoricalRecord
from .filters import LandOwnerFilter
from rest_framework.decorators import authentication_classes ,permission_classes
from apps.places.models import District
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
    filterset_fields = ['owner', 'status', 'id', 'ubigeo','cpm','cup']
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

# @authentication_classes([])
# @permission_classes([])

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
    queryset = Land.objects.all()
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
        without_mapping_records = self.filter_queryset(Land.objects.filter(status=0)).count()
        inactive_records =  self.filter_queryset(Land.objects.filter(status=3)).count()
        mapping_records = total_records - without_mapping_records -inactive_records
        return {
            'total_records': total_records,
            'mapping_records': mapping_records,
            'without_mapping_records': without_mapping_records,
            'inactive_records':inactive_records,
        }


@authentication_classes([])
@permission_classes([])
class SRTMViewSet(GenericViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    


    @action(methods=['POST'], detail=False, url_path='crear-contribuyente')
    def create_owner(self, request, *args, **kwargs):
        document_type= request.data.get('doc_identidad_id',None)
        document_type = '01' if document_type ==1 else '06' if document_type ==2 else   document_type 

        data = {
            'sec_ejec':request.data.get('municipalidad_id',None), 
            'code' : request.data.get('contribuyente_numero',None),
            'ubigeo' : request.data.get('ubigeo_registro',None),
            'tipo_contribuyente':  request.data.get('tip_contribuyente_id',None),
            'document_type' : document_type,
            'dni':request.data.get('num_doc_identidad',None),
            'name': request.data.get('nombres',None) if document_type == '01' else request.data.get('razon_social',None)    ,
            'paternal_surname': request.data.get('ape_paterno',None),
            'maternal_surname': request.data.get('ape_materno',None),
            'domicilios': request.data.get('domicilios',[]),
            'contactos': request.data.get('contactos',[]),
        }

        
        serializer = LandOwnerSRTMSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        a = serializer.save()
        return Response({'message':'Contribuyente creado','status':True}, status=status.HTTP_201_CREATED)
    
    
    @action(methods=['POST'], detail=False, url_path='guardar-predio-contribuyente',url_name='guardar-predio-contribuyente')
    def save_land_owner(self, request, *args, **kwargs):
        records=request.data    
        #print('records>>',records) 
        for record in records:
            #print('record>>',record)
            code_owner = record.get('contribuyente_numero',None)
            cpu = record.get('codigo_predio_unico',None)
            cpm = record.get('codigo_predio_municipal',None)
            ubigeo = record.get('ubigeo_predio')


            data = {
                'predio_codigo' :record.get('predio_codigo',None),
                'sec_ejec' :record.get('municipalidad_id',None),
                'cup' : record.get('codigo_predio_unico',None),
                'cpm' : record.get('codigo_predio_municipal',None),
                'ubigeo' : record.get('ubigeo_predio',None),
                'area_terreno':record.get('area_terreno',None),
                'area_tot_terr_comun': record.get('area_tot_terr_comun',None),
                'area_construida': record.get('area_construida',None),
                'area_tot_cons_comun': record.get('area_tot_cons_comun',None),
                'por_propiedad': record.get('por_propiedad',None),
                'tip_transferencia': record.get('tip_transferencia_id',None),
                'tip_uso_predio': record.get('tip_uso_predio_id',None),
                'tip_propiedad': record.get('tip_propiedad_id',None),
                'fec_transferencia': record.get('fec_transferencia',None),
                'longitud_frente': record.get('longitud_frente',None),
                'cantidad_habitantes': record.get('cantidad_habitantes',None),
                'pre_inhabitable': record.get('pre_inhabitable',None),
                'par_registral': record.get('par_registral',None),
                'numero_dj': record.get('numero_dj',None),
                'fecha_dj': record.get('fecha_dj',None),
                'usuario_auditoria': record.get('usuario_auditoria',None),
                'estado_dj': record.get('estado_dj_id'),
                'motivo_dj': record.get('motivo_dj_id'),
            }



            
            
            owners=LandOwner.objects.filter(code =code_owner,ubigeo = ubigeo)
            districts=District.objects.filter( code=ubigeo)
            
            lands=[]
            if cpu is not None:
                lands=Land.objects.filter(cup =cpu,ubigeo = ubigeo)
            
            elif cpm is not None:
                lands=Land.objects.filter(cpm =cpm,ubigeo = ubigeo)
            
            
            if len(owners)==0:
                return Response({'message':'Contribuyente no existe','status':False}, status=status.HTTP_400_BAD_REQUEST)
            else:
                owner = owners[0]
            

            if len(lands)==0:
                return Response({'message':'Predio no existe','status':False}, status=status.HTTP_400_BAD_REQUEST)
            else:
                land = lands[0]
            
            if len(districts)==0:
                return Response({'message':'Distrito no existe' ,'status':False }, status=status.HTTP_400_BAD_REQUEST)
            else:
                district = districts[0]
            
            
            data['land']= land.id
            data['ubigeo']=district.code
            data['owner']=owner.id
            #dataSerializer=LandOwnerDetail(owner=owner, land=land, ubigeo=district)
            serializer = LandOwnerDetailSRTMSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response({'message':'Registros guardados' ,'status':True }, status=status.HTTP_201_CREATED)
    
        
    @action(methods=['POST'], detail=False, url_path='guardar-nivel-construccion',url_name='guardar-nivel-construccion')
    def save_nivel_construccion(self, request, *args, **kwargs):
        code_owner = request.data.get('codigo_contribuyente',None)
        ubigeo = request.data.get('ubigeo',None)
        cpu = request.data.get('codigo_predio_unico',None)
        cpm = request.data.get('codigo_predio_municipal',None)


        owners=LandOwner.objects.filter(code =code_owner,ubigeo = ubigeo)
        lands=[]
        if cpu is not None:
            lands=Land.objects.filter(cup =cpu,ubigeo = ubigeo)
        
        elif cpm is not None:
            lands=Land.objects.filter(cpm =cpm,ubigeo = ubigeo)

        if len(owners)==0:
            return Response({'message':'Contribuyente no existe','status':False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            owner = owners[0]

        if len(lands)==0:
            return Response({'message':'Predio no existe','status':False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            land = lands[0]

        detalles=LandOwnerDetail.objects.filter(land=land,owner=owner)

        if len(detalles)==0:
            return Response({'message':'No existe la relacion entre el predio y contribuyente','status':False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            obj = detalles[0]

        #obj=LandOwnerDetail.objects.filter(land=land,owner=owner)

        
        data=request.data
        data['land_owner_detail']= obj.id

        serializer = LandNivelConstruccionSerializer(data=data, many = False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Registro guardado' ,'status':True }, status=status.HTTP_201_CREATED)


    @action(methods=['POST'], detail=False, url_path='guardar-deuda-contribuyente',url_name='guardar-deuda-constribuyente')
    def save_deuda(self, request, *args, **kwargs):
        code_owner = request.data.get('codigo_contribuyente',None)
        ubigeo = request.data.get('ubigeo',None)
        
        owners=LandOwner.objects.filter(code =code_owner,ubigeo = ubigeo)
        if len(owners)==0:
            return Response({'message':'Contribuyente no existe','status':False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            owner = owners[0]

        

        data=request.data
        data['owner']=owner.id

        serializer = OwnerDeudaSerializer(data=data, many = False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Registro guardado' ,'status':True }, status=status.HTTP_201_CREATED)