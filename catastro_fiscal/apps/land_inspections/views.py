from django.shortcuts import render
from rest_framework.decorators import authentication_classes ,permission_classes
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import CamelCaseOrderFilter
from .models import Ticket , Location,LandInspection, RecordOwnerShip,LandSupply
from .serializers import TicketSerializer, TicketListSerializer,TicketRetriveSerializer,LocationSerializer,RecordOwnerShipRetriveSerializer ,LandInspectionSerializer,LocationRetriveSerializer,RecordOwnerShipSerializer,  LandSupplyRetriveSerializer, LandSupplySerializer
from rest_framework.viewsets import GenericViewSet ,ModelViewSet
import django_filters

class TicketFilter(django_filters.FilterSet):
    codTicket = django_filters.CharFilter(field_name="cod_ticket",lookup_expr='icontains')
    codEstTrabajoTicket= django_filters.CharFilter(field_name="cod_est_trabajo_ticket",lookup_expr='exact')
    class Meta:
        model = Ticket
        fields = ['codTicket', 'codEstTrabajoTicket']

# Create your views here.
@authentication_classes([])
@permission_classes([])

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_class = TicketFilter
    #filterset_fields = ['cod_ticket','cod_est_trabajo_ticket','cod_ticket__contains']
    search_fields = ['cod_ticket']
    
    def get_serializer_class(self):
        if self.action == 'list' :
            return TicketListSerializer
        elif self.action == 'retrieve' :
            return TicketRetriveSerializer
        
        else:
            return TicketSerializer 


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['cod_ticket']
    search_fields = ['cod_ticket']
    def get_serializer_class(self):

        if self.action == 'retrieve' :
            return LocationRetriveSerializer
        
        else:
            return LocationSerializer 

class RecordOwnerShipViewSet(ModelViewSet):
    queryset = RecordOwnerShip.objects.all()
    serializer_class = RecordOwnerShipRetriveSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['cod_ubicacion']
    search_fields = ['cod_ubicacion']
    
    def get_serializer_class(self):
        if self.action == 'retrieve' :
            return RecordOwnerShipRetriveSerializer
        
        else:
            return RecordOwnerShipSerializer 

class LandInspectionViewSet(ModelViewSet):
    queryset = LandInspection.objects.all()
    serializer_class = LandInspectionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]


class LandSupplyViewSet(ModelViewSet):
    queryset = LandSupply.objects.all()
    serializer_class = LandSupplySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    def get_serializer_class(self):
        if self.action == 'retrieve' :
            return LandSupplyRetriveSerializer
        else:
            return LandSupplySerializer