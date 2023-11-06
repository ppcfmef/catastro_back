from django.shortcuts import render
from rest_framework.decorators import authentication_classes ,permission_classes
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import CamelCaseOrderFilter
from .models import Ticket , Location,LandInspection, RecordOwnerShip
from .serializers import TicketSerializer, LocationSerializer,RecordOwnerShipSerializer ,LandInspectionSerializer
from rest_framework.viewsets import GenericViewSet ,ModelViewSet,RecordOwnerShip
# Create your views here.
@authentication_classes([])
@permission_classes([])

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['cod_ticket']
    search_fields = ['cod_ticket']


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['cod_ticket']
    search_fields = ['cod_ticket']

class RecordOwnerShipViewSet(ModelViewSet):
    queryset = RecordOwnerShip.objects.all()
    serializer_class = RecordOwnerShipSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['cod_ubicacion']
    search_fields = ['cod_ubicacion']

class LandInspectionViewSet(ModelViewSet):
    queryset = LandInspection.objects.all()
    
    serializer_class = LandInspectionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]


