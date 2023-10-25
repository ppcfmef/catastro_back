from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet ,ModelViewSet
from rest_framework.decorators import action
from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import CamelCaseOrderFilter
from core.views import CustomSerializerMixin
from core.views import CustomListMixin
from apps.lands.models import Land
from .models import Result,ApplicationLandDetail,ApplicationResultDetail,Application,ApplicationObservationDetail
from apps.lands.serializers import LandSerializer
from rest_framework.decorators import authentication_classes ,permission_classes
from django.forms.models import model_to_dict
from .serializers import (
    ApplicationSerializer,ApplicationListSerializer,LandListSerializer,ResultSerializer,LandApplicationSerializer,LandByApplicationListSerializer,ApplicationObservationDetailSerializer,ResultDetailCustomSerializer
)


@authentication_classes([])
@permission_classes([])
class ApplicationViewSet( ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['id' , 'ubigeo','id_status','id_type']
    
    def get_serializer_class(self):
        if self.action == 'list' :
            return ApplicationListSerializer
        return ApplicationSerializer 
        
    
    def list(self, request, *args, **kwargs):
        cpm = self.request.query_params.get('cpm',None)
        #print('cup>>>',cup)
        if cpm is not None:
            try:
                id_apps=ApplicationLandDetail.objects.filter(land__cpm=cpm).values_list('application_id',flat=True)
                a=Application.objects.filter(id__in=id_apps)
                queryset = self.filter_queryset(a)
                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response(serializer.data)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)
            except:    
                Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
            
         

    def create(self,request, *args, **kwargs):
        lands = request.data.get('lands')
        results = request.data.get('results')
        application = request.data.get('application')
        #try:
        serializer=self.get_serializer(data=application)
        serializer.is_valid(raise_exception=True)
        serializer.save()
            
        for land in lands:
            try:
                ApplicationLandDetail.objects.create(application_id= serializer.data['id'], land_id = land['id'])
            except:
                Application.objects.filter(id= serializer.data['id']).delete()
        for result in results:
            try:
                rserializer=ResultSerializer(data=result)
                rserializer.is_valid(raise_exception=True)
                rserializer.save()
                ApplicationResultDetail.objects.create(application_id= serializer.data['id'], result_id = rserializer.data['id'])
            except:
                Application.objects.filter(id= serializer.data['id']).delete()
        
         
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(methods=['POST'], detail=False, url_path='upload-file')
    def upload_file(self,request, *args, **kwargs):
            
        id_app=request.data['id_app']
        a=Application.objects.get(id=id_app)
        a.support=request.data['file']
        a.save()
        return Response({'success':True})

    @action(methods=['POST'], detail=False, url_path='update-application-attended')
    def update_application_attended(self,request, *args, **kwargs):
        id_app=request.data.get('id')
        results = request.data.get('results')
        try:
            a=Application.objects.get(id=id_app)
            if(a.id_status==2):
                return Response({'error': 'la solicitud ya se encuentra atendida'}, status=status.HTTP_400_BAD_REQUEST)    
            else:
                if a.id_type == 1:
                    for result in results:
                        r=Land.objects.get(ubigeo_id= result.get('ubigeo', None),cpm= result.get('cod_pre', None))
                        r.longitude = result.get('coord_x', None)
                        r.latitude = result.get('coord_y', None)
                        r.save()
                
                elif a.id_type == 4:
                    lands_id = ApplicationLandDetail.objects.filter(application_id=id_app).values_list('land_id', flat=True)
                    print('lands_id>>>',lands_id)
                    lands = Land.objects.filter(id__in=list(lands_id))
                    lands.update(status=3)


                else:
                    lands_id = ApplicationLandDetail.objects.filter(application_id=id_app).values_list('land_id', flat=True)
                    lands = Land.objects.filter(id__in=list(lands_id))
                    lands.update(status=3)
                    for result in results:
                        data={
                            'ubigeo_id':result.get('ubigeo', None),
                            'habilitacion_name':result.get('nom_uu', None),
                            'reference_name':result.get('nom_ref', None)   ,
                            'cup':result.get('cod_cpu', None),
                            'cod_street':result.get('cod_via', None),
                            'street_type_id':result.get('tip_via', None),
                            'urban_mza':result.get('mzn_urb', None),
                            'cod_sect':result.get('cod_sect', None),
                            'cod_uu':result.get('cod_uu', None),
                            'uu_type':result.get('tipo_uu', None),
                            'municipal_address':result.get('dir_mun', None),
                            'cod_mzn':result.get('cod_mzn', None),
                            'cod_land':result.get('cod_lote', None),
                            'cpm':result.get('cod_pre', None),
                            'urban_address':result.get('dir_urb', None),
                            'urban_lot_number':result.get('lot_urb', None),
                            'longitude':result.get('coord_x', None),
                            'latitude':result.get('coord_y', None),
                            'cod_uu':result.get('cod_uu', None),
                            'street_name':result.get('nom_via', None),
                            'status':1,
                            'source':'mantenimiento_pre'
                        }
                            
                        l=Land(**data)
                        serializer=LandSerializer(data =model_to_dict(l), many=False)
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                    

                a.id_status=2
                a.save()
                return Response({'success':True})
        except Application.DoesNotExist:
            return Response({'error': 'No se encontro la solicitud'}, status=status.HTTP_400_BAD_REQUEST)
        
@authentication_classes([])
@permission_classes([])
class LandViewSet(ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['id','cpm','ubigeo']
    search_fields = ['ubigeo__code','ubigeo__name','cpm' ,'cup']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return LandListSerializer
        return LandApplicationSerializer
    
    @action(methods=['GET'], detail=False, url_path='has-not-applications')
    def get_has_not_applications(self, request, *args, **kwargs):
        lands_id = ApplicationLandDetail.objects.values_list('land_id', flat=True)
        lands = self.get_queryset().exclude(id__in=list(lands_id))
         
        queryset = self.filter_queryset(lands)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = LandListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
    @action(methods=['GET'], detail=False, url_path='lands-by-application/(?P<application_id>[0-9]+)')
    def get_lands_by_application(self, request, *args, **kwargs):
        application_id = kwargs.get('application_id')
        print('application_id>>>',application_id)
        lands_id = ApplicationLandDetail.objects.filter(application_id=application_id).values_list('land_id', flat=True)
        print('lands_id>>>',lands_id)
        lands = self.get_queryset().filter(id__in=list(lands_id))
        queryset = self.filter_queryset(lands)
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = LandByApplicationListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = LandByApplicationListSerializer(queryset, many=True)
        return Response(serializer.data)

@authentication_classes([])
@permission_classes([])
class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    
    @action(methods=['GET'], detail=False, url_path='results-by-application/(?P<application_id>[0-9]+)')
    def get_results_by_application(self, request, *args, **kwargs):
        application_id = kwargs.get('application_id')
        
        lands_id = ApplicationResultDetail.objects.filter(application_id=application_id).values_list('result_id', flat=True)
        
        lands = self.get_queryset().filter(id__in=list(lands_id))
        queryset = self.filter_queryset(lands)
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = ResultDetailCustomSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ResultDetailCustomSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
@authentication_classes([])
@permission_classes([])
class ApplicationObservationDetailViewSet(ModelViewSet):
    queryset = ApplicationObservationDetail.objects.all()
    serializer_class= ApplicationObservationDetailSerializer
    
    def create(self,request, *args, **kwargs):
        application_id=request.data['application_id']
        description=request.data['description']
        a=ApplicationObservationDetail(application_id= application_id,description=description)
        a.save()
    
        a.img=request.data['img']
        a.save()
        serializer=self.get_serializer(data =model_to_dict(a), many=False)
        serializer.is_valid(raise_exception=True)
        app=Application.objects.get(id=application_id)
        app.id_status= 3
        app.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED )