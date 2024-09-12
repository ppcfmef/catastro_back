from django.shortcuts import render

from rest_framework.decorators import authentication_classes ,permission_classes,action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import CamelCaseOrderFilter
from .models import Ticket , Location,LandInspection, RecordOwnerShip,LandSupply,LandCharacteristic ,LocationPhoto,LandFacility
from apps.places.models import District
from .serializers_results import TicketSerializer, TicketListSerializer,TicketRetriveSerializer,LocationSerializer,RecordOwnerShipRetriveSerializer ,LandInspectionSerializer,LocationRetriveSerializer,RecordOwnerShipSerializer,  LandSupplyRetriveSerializer, LandSupplySerializer
from rest_framework.viewsets import GenericViewSet ,ModelViewSet
import django_filters
from core.utils.exports import render_to_pdf


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

@authentication_classes([])
@permission_classes([])
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


@authentication_classes([])
@permission_classes([])
class ExportPdfViewSet(GenericViewSet):
    @action(methods=['post'], detail=False, url_path='generar_notificacion_subvaluado')
    def generar_notificacion_subvaluado(self, request, *args, **kwargs):
        
        username=request.data.get('username',None)
        cod_ticket=request.data.get('cod_ticket',None)
        cod_tit=request.data.get('cod_tit',None)
        texto=request.data.get('texto',None)
        contribuyente =request.data.get('contribuyente',None)
        direccion =request.data.get('direccion',None)
        context_dict = { }

        
        

        if cod_ticket is not None:
            t=Ticket.objects.get(cod_ticket=cod_ticket )
            if t is not None and cod_tit is not None:
               
                r=RecordOwnerShip.objects.get(cod_tit = cod_tit)
                recordOwnerShipSerializer=RecordOwnerShipRetriveSerializer(r,many=False)
                if r is not None:
                    l=Location.objects.get(cod_ubicacion=r.cod_ubicacion)
                    locationSerializer=LocationRetriveSerializer(l,many=False)
                    fotos = LocationPhoto.objects.filter(cod_ubicacion=r.cod_ubicacion)
                    # d=District.objects.get(code = r.ubigeo)
                    # fotos = []
                    # fotos2 = []
                    
                    # fotos = LocationPhoto.objects.filter(cod_ubicacion=r.cod_ubicacion)
                    
                    # if len(fotos)>0:
                    #     fotos = fotos[:3]
                    #     if len(fotos)>3:
                    #         fotos2 = fotos[3:]
                            
                    
                    # i=LandFacility.objects.filter(cod_tit=r.cod_tit ) 
                    # if r is not None:
                    #     c=LandCharacteristic.objects.get(cod_tit=r.cod_tit )
                    # else:
                    #     c={}
                else:
                    r={}
                t.nro_notificacion=t.nro_notificacion+1
                t.save()    
                context_dict = { 'username' : username, 'cod_ticket':cod_ticket ,
                                'ticket':t,
                                'data_registro_titularidad':recordOwnerShipSerializer.data,
                                # 'caracteristicas':c,
                                'ubicacion':locationSerializer.data,
                                'fotos':fotos,
                                # 'instalaciones':i,
                                
                                'texto':texto,
                                'nro_notificacion': (t.nro_notificacion),'contribuyente':contribuyente,'direccion': None}
        return render_to_pdf('pdf/notificacion_subvaluado.html', context_dict)
        
        
    @action(methods=['post'], detail=False, url_path='generar_notificacion')
    def generar_notificacion(self, request, *args, **kwargs):
        usuario=request.data.get('usuario',None)
        rol=request.data.get('rol',None)
        cod_ticket=request.data.get('cod_ticket',None)
        cod_tit=request.data.get('cod_tit',None)
        texto=request.data.get('texto',None)
        id_land=request.data.get('id_land',None)
        contribuyente =request.data.get('contribuyente',None)
        context_dict = { }
        if cod_ticket is not None:
            t=Ticket.objects.get(cod_ticket=cod_ticket )
            if t is not None and cod_tit is not None:
               
                r=RecordOwnerShip.objects.get(cod_tit = cod_tit)
                if r is not None:
                    fotos = LocationPhoto.objects.filter(cod_ubicacion=r.cod_ubicacion,cod_tipo_foto__in =[1])
                    #print('fotos>>',fotos)
                    l=Location.objects.get(cod_ubicacion=r.cod_ubicacion)
                    d=District.objects.get(code = r.ubigeo)
                    land=LandInspection.objects.get(id = id_land)
                    if r is not None:
                        c=LandCharacteristic.objects.get(cod_tit=r.cod_tit )
                    else:
                        c={}
                 
             
                        
                    
                else:
                    r={}
                t.nro_notificacion=t.nro_notificacion+1
                t.save()    
                #print('c>>',c)
                context_dict = { 'usuario' : usuario,'rol':rol, 'cod_ticket':cod_ticket ,'ticket':t,'ubicacion':l,'texto':texto,'nro_notificacion': (t.nro_notificacion),'distrito': d,'contribuyente':contribuyente,'fotos':fotos,'caracteristicas':c,'land':land}
                
                
        return render_to_pdf('pdf/notificacion.html', context_dict)       