from django.db import transaction
from rest_framework import serializers
from .models import Ticket, TicketSendStation, LandOwnerInspection, Location, LocationPhoto, LandFacility, SupplyType, LandSupply, LandFacility, LandInspectionType, RecordOwnerShip, LandCharacteristic, LandInspection,LocationPhoto,LandOwnerDetailInspection
from apps.lands.models import Land, LandOwner,LandOwnerDetail,MasterCodeStreet
from apps.lands.serializers import LandOwnerDetailSerializer
from core.utils.formato import Format

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
    tipo_sumi = serializers.CharField(source='cod_tipo_sumi.desc_tipo_sumi',allow_null=True)
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
    
    tipo_predio_nombre = serializers.CharField(source='cod_tipo_predio.name',allow_null=True)

    clase_uso_nombre  =  serializers.CharField(source='codigo_clase_uso.name',allow_null=True)
    subclase_uso_nombre = serializers.CharField(source='codigo_sub_clase_uso.name',allow_null=True)
    tipo_uso_nombre = serializers.CharField(source='codigo_uso.name',allow_null=True)
    
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
    tip_obra_complementaria_nombre = serializers.CharField(source='tip_obra_complementaria.name')
    tip_material_nombre = serializers.CharField(source='tip_material.name')
    est_conservacion_nombre = serializers.CharField(source='est_conservacion.name')
    class Meta:
        model = LandFacility
        fields = '__all__'


class LandCharacteristicSerializer(serializers.ModelSerializer):
    estado_conserva_nombre =  serializers.CharField(source='estado_conserva.name',allow_null=True)
    material_pred_nombre = serializers.CharField(source='material_pred.name',allow_null=True)
    class Meta:
        model = LandCharacteristic
        fields = '__all__'


class LocationPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationPhoto
        fields = '__all__'



# class LandOwnerDetailSerializer(serializers.ModelSerializer):
#     contribuyente = LandOwnerSerializer(source='owner',many=False, read_only=True)
#     class Meta:
#         model = LandOwnerDetail
#         fields = '__all__'

class LandPadronRetrieveSerializer(serializers.ModelSerializer):
    #predio_contribuyente = LandOwnerDetailSerializer(many=True, read_only=True)
    predio_contribuyente = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    tipo_predio_nombre = serializers.CharField(source='cod_tipo_predio.name',allow_null=True)
    class Meta:
        model = Land
        fields = '__all__'
        
    
    def get_address(self,obj):
        return '{street_type} {street_name} {municipal_number} {urban_mza} {urban_lot_number}'.format(street_type=obj.street_type.name,street_name = obj.street_name,municipal_number =obj.municipal_number,urban_mza ='Mz.{}'.format(obj.urban_mza) if Format.isNoneOrBlank(obj.urban_mza) else '' ,urban_lot_number ='Lote {}'.format( obj.urban_lot_number) if  Format.isNoneOrBlank(obj.urban_lot_number)  else '' )
    
    def get_predio_contribuyente(self, obj):
        dj=LandOwnerDetail.objects.filter(land_id=obj.id,estado_dj=1)
        return LandOwnerDetailSerializer(dj,many=True).data


    
class RecordOwnerShipRetriveSerializer(serializers.ModelSerializer):
    caracteristicas= LandCharacteristicSerializer(many=False,read_only=True)
    instalaciones  = LandFacilitySerializer(many=True,read_only=True)
    suministro = LandSupplyRetriveSerializer(many=False,read_only=True)
    predio_inspeccion = LandInspectionSerializer(many=False,read_only=True)
    tipo_tit = serializers.CharField(source='cod_tipo_tit.desc_tipo_tit',allow_null=True)
    predio_padron = serializers.SerializerMethodField(read_only=True)

    municipal_name = serializers.CharField(source='ubigeo.municipal_name',allow_null=True)
    class Meta:
        model = RecordOwnerShip
        fields = '__all__'
        
    # def get_tipo_tit(self, obj):
    #     owner_ship_type=OwnerShipType.objects.filter(cod_tipo_tit=obj.cod_tipo_tit)
    #     if len(owner_ship_type)>0:
    #         return owner_ship_type[0].desc_tipo_tit
        
    def get_predio_padron(self, obj):
        lands=LandInspection.objects.filter(cod_tit=obj.cod_tit)
        if len(lands)>0:
            land=lands[0]
            # print('land.cod_cpu',land.cod_cpu)
            # print('land.cod_pre',land.cod_pre)
            # print('land.ubigeo',land.ubigeo)

            if land.cod_cpu =='' or land.cod_cpu is None   :
                return None
            else:
                landPadrons=Land.objects.filter(cup=land.cod_cpu, ubigeo =land.ubigeo)
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
    address = serializers.SerializerMethodField()
    class Meta:
        model = Location
        fields = '__all__'
    
    
        
    def get_address(self,obj):
        street_type=MasterCodeStreet.objects.get(id= obj.cod_tip_via)
        return """{street_type} {street_name} {municipal_number} {urban_mza} {urban_lot_number}""".format(street_type=street_type.name,street_name = obj.nom_via,
                                                                                                        municipal_number = obj.num_mun if Format.isNoneOrBlank(obj.num_mun) else '' ,
                                                                                                        urban_mza ='Mz.{}'.format(obj.mzn_urb) if Format.isNoneOrBlank(obj.mzn_urb) else '', 
                                                                                                        urban_lot_number ='Lote {}'.format( obj.lot_urb) if  Format.isNoneOrBlank(obj.lot_urb)   else '',
                                                                                                        )
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    estTrabajoTicket = serializers.CharField(source='cod_est_trabajo_ticket.desc_est_trabajo_ticket',allow_null=True)
    tipoTicket = serializers.CharField(source='cod_tipo_ticket.desc_tipo_ticket',allow_null=True)
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketListSerializer(serializers.ModelSerializer):
    tipoTicket = serializers.CharField(source='cod_tipo_ticket.desc_tipo_ticket',allow_null=True)
    estTrabajoTicket = serializers.CharField(source='cod_est_trabajo_ticket.desc_est_trabajo_ticket',allow_null=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketRetriveSerializer(serializers.ModelSerializer):
    tipoTicket = serializers.CharField(source='cod_tipo_ticket.desc_tipo_ticket',allow_null=True)
    total_ubicaciones = serializers.SerializerMethodField(read_only=True)
    ubicaciones = LocationRetriveSerializer(many=True, read_only=True)
    # ubicaciones = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Ticket
        fields = '__all__'

    def get_total_ubicaciones(self, obj):
        return len(Location.objects.filter(cod_ticket=obj.cod_ticket))

