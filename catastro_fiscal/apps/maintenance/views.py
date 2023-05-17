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
    filterset_fields = ['id' , 'ubigeo']
    
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
            ApplicationLandDetail.objects.create(application_id= serializer.data['id'], land_id = land['id'])
        for result in results:
            rserializer=ResultSerializer(data=result)
            rserializer.is_valid(raise_exception=True)
            rserializer.save()
            ApplicationResultDetail.objects.create(application_id= serializer.data['id'], result_id = rserializer.data['id'])
        
        
         
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(methods=['POST'], detail=False, url_path='upload-file')
    def upload_file(self,request, *args, **kwargs):
            
        id_app=request.data['id_app']
        a=Application.objects.get(id=id_app)
        a.support=request.data['file']
        a.save()
        return Response({'success':True})

@authentication_classes([])
@permission_classes([])
class LandViewSet(ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['id','cpm','ubigeo']
    search_fields = ['ubigeo__name','cpm' ]
    
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