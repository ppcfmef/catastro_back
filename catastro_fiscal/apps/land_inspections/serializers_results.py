from django.db import transaction
from rest_framework import serializers
from .models import Ticket, TicketSendStation, LandOwnerInspection, Location, LocationPhoto, LandFacility, SupplyType, LandSupply, LandFacility, LandInspectionType, RecordOwnerShip, LandCharacteristic, LandInspection,LocationPhoto,LandOwnerDetailInspection
from apps.lands.models import Land, LandOwner,LandOwnerDetail


class LandSupplyOwnerSerializer(serializers.ModelSerializer):
    ap_pat =serializers.CharField(source='paternal_surname')
    ap_mat = serializers.CharField(source='maternal_surname')
    nombre = serializers.CharField(source='name')
    doc_iden = serializers.CharField(source='dni')

    class Meta:
        model = LandOwner
        fields = ['id','ap_pat','ap_mat','nombre','doc_iden','email','phone']

class LandOwnerSerializer(serializers.ModelSerializer):
    ap_pat =serializers.CharField(source='paternal_surname')
    ap_mat = serializers.CharField(source='maternal_surname')
    nombre = serializers.CharField(source='name')
    doc_iden = serializers.CharField(source='dni')

    class Meta:
        model = LandOwner
        fields = ['id','ap_pat','ap_mat','nombre','doc_iden','email','phone']

class LandSupplyRetriveSerializer(serializers.ModelSerializer):
    tipo_sumi = serializers.CharField(source='cod_tipo_sumi.desc_tipo_sumi')
    contribuyente = LandSupplyOwnerSerializer(source='cod_contr',many=False, read_only=True)
    class Meta:
        model = LandSupply
        fields = '__all__'

class LandSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = LandSupply
        fields = '__all__'
        

class LandOwnerInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandOwnerInspection
        fields = '__all__'
        
class LandOwnerDetailInspectionSerializer(serializers.ModelSerializer):
    contribuyente = LandOwnerInspectionSerializer(source='cod_contr_inspec',many=False, read_only=True)
    class Meta:
        model = LandOwnerDetailInspection
        fields = '__all__'



class LandInspectionSerializer(serializers.ModelSerializer):
    predio_contribuyente = LandOwnerDetailInspectionSerializer(many=True, read_only=True)
    #contribuyente= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = LandInspection
        fields = '__all__'
        
    # def get_contribuyente(self, obj):
    #     landOwners = LandOwnerDetailInspection.objects.filter(cod_pred_inspec=obj.id)
    #     if len(landOwners)>0:
            
    #         owners=LandOwnerInspection.objects.filter(id=landOwners[0].cod_contr_inspec.id)
    #         if len(owners)>0:
                
                
    #             return LandOwnerInspectionSerializer(data=owners,many=True)
    #         else:
    #             return None
        
    #     else:
    #         return None
        
        
class LandFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LandFacility
        fields = '__all__'


class LandCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandCharacteristic
        fields = '__all__'


class LocationPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationPhoto
        fields = '__all__'



class LandOwnerDetailSerializer(serializers.ModelSerializer):
    contribuyente = LandOwnerSerializer(source='owner',many=False, read_only=True)
    class Meta:
        model = LandOwnerDetail
        fields = '__all__'

class LandPadronRetrieveSerializer(serializers.ModelSerializer):
    predio_contribuyente = LandOwnerDetailSerializer(many=True, read_only=True)
    address = serializers.SerializerMethodField()
    class Meta:
        model = Land
        fields = '__all__'
        
    
    def get_address(self,obj):
        return '{street_type} {street_name} {municipal_number} {urban_mza} {urban_lot_number}'.format(street_type=obj.street_type,street_name = obj.street_name,municipal_number = obj.municipal_number if obj.municipal_number is not None else '' ,urban_mza =' Mz.{}'.format(obj.urban_mza) if obj.urban_mza is not None else '' ,urban_lot_number =' Lote {}'.format( obj.urban_lot_number) if  obj.urban_lot_number is not None else '' )


class RecordOwnerShipRetriveSerializer(serializers.ModelSerializer):
    caracteristicas= LandCharacteristicSerializer(many=False,read_only=True)
    instalaciones  = LandFacilitySerializer(many=True,read_only=True)
    suministro = LandSupplyRetriveSerializer(many=False,read_only=True)
    predio_inspeccion = LandInspectionSerializer(many=False,read_only=True)
    tipoTit = serializers.CharField(source='cod_tipo_tit.desc_tipo_tit')
    predio_padron = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = RecordOwnerShip
        fields = '__all__'
        
    def get_predio_padron(self, obj):
        lands=LandInspection.objects.filter(cod_tit=obj.cod_tit)
        if len(lands)>0:
            land=lands[0]
            # print('land.cod_pre',land.cod_pre)
            # print('land.ubigeo',land.ubigeo)
            landPadrons=Land.objects.filter(cpm=land.cod_pre, ubigeo =land.ubigeo)
            if len(landPadrons)>0:
            
                return LandPadronRetrieveSerializer(landPadrons[0],many=False).data
            else:
                return None
        else:
            return None

class RecordOwnerShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecordOwnerShip
        fields = '__all__'
        

        
class LocationRetriveSerializer(serializers.ModelSerializer):
    fotos = LocationPhotoSerializer(many=True, read_only=True)
    registros_titularidad = RecordOwnerShipRetriveSerializer(many=True, read_only=True)
    class Meta:
        model = Location
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    tipoTicket = serializers.CharField(source='cod_tipo_ticket.desc_tipo_ticket')
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketListSerializer(serializers.ModelSerializer):
    tipoTicket = serializers.CharField(source='cod_tipo_ticket.desc_tipo_ticket')
    estTrabajoTicket = serializers.CharField(source='cod_est_trabajo_ticket.desc_est_trabajo_ticket')

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketRetriveSerializer(serializers.ModelSerializer):
    tipoTicket = serializers.CharField(source='cod_tipo_ticket.desc_tipo_ticket')
    total_ubicaciones = serializers.SerializerMethodField(read_only=True)
    ubicaciones = LocationRetriveSerializer(many=True, read_only=True)
    # ubicaciones = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Ticket
        fields = '__all__'

    def get_total_ubicaciones(self, obj):
        return len(Location.objects.filter(cod_ticket=obj.cod_ticket))

    # def get_ubicaciones(self, obj):
    #     ubicaciones = Location.objects.filter(cod_ticket=obj.cod_ticket)
    #     resumen_ubicaciones = []

    #     for ubicacion in ubicaciones:
    #         records = RecordOwnerShip.objects.filter(cod_ubicacion=ubicacion.cod_ubicacion)
    #         totalCasos = len(records)
    #         resumen_ubicaciones.append({'codUbicacion': ubicacion.cod_ubicacion,'totalCasos': totalCasos,'state': 0})

    #     return resumen_ubicaciones