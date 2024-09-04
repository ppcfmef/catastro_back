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
from apps.lands.serializers import LandSerializer
from rest_framework.decorators import authentication_classes ,permission_classes
from django.forms.models import model_to_dict
from .serializers import (
    DistrictAnalisysSerializer, LandListAnalisysSerializer,LandAnalisysSerializer
)
from django.db.models import Q,Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apps.places.models import  District
from apps.users.models import User
from apps.users.serializers import UserDetailSerializer,UserSerializer
        
@authentication_classes([])
@permission_classes([])
class LandGapAnalisysViewSet(ModelViewSet):
    queryset = Land.objects.all().filter(Q(status=0,status_gap_analisys__isnull =False) |  Q(status=1,status_gap_analisys =1) )
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]

    
    #filterset_fields = ['id','cpm','ubigeo','status','status_gap_analisys']
    
    filterset_fields = {
        'id':['exact'],
        'cpm':['exact'],
        'ubigeo':['exact'],
        'status_gap_analisys':['in','exact']
    }
    search_fields = ['cpm' ,'street_name','habilitacion_name','street_type__name']
    
    def get_serializer_class(self):
        if self.action == 'list' :
            return LandListAnalisysSerializer
        return LandAnalisysSerializer
    
    @action(methods=['GET'], detail=False, url_path='stadisticts_gap_analisys')
    def stadisticts_gap_analisys(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.queryset)
        data=queryset.values('status_gap_analisys').annotate(count=Count("id"))
        return Response(data,status= status.HTTP_200_OK)


 
@authentication_classes([])
@permission_classes([])
class DistrictViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictAnalisysSerializer
    #pagination_class = None
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['province','code','name']
    search_fields = ['name','province__name','province__department__name','code']

@authentication_classes([])
@permission_classes([])
class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    list_serializer_class = UserDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_active', 'role', 'institution', 'department', 'province', 'district','district__code','is_mobile_staff','dni']
    search_fields = ['dni', 'district__code', 'district__name']
