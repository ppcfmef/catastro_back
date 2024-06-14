from django.db import transaction
from rest_framework import serializers
from .models import UploadHistory, Land, LandOwner, OwnerAddress, LandAudit, LandOwnerDetail , Domicilio, Contacto , LandNivelConstruccion,OwnerDeuda
from apps.maintenance.models import ApplicationLandDetail , Application
from .tasks import process_upload_tenporal, process_upload_land
from .services.upload_temporal import UploadTemporalService
from .services.upload_land import UploadLandService

from apps.maintenance.serializers import ApplicationSerializer,ApplicationListSerializer

class UploadHistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHistory
        fields = '__all__'


class UploadHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHistory
        fields = ('id', 'file_upload',)

    def create(self, validated_data):
        username = getattr(self.context.get('request'), 'user', None)
        validated_data.update({
            'username': username
        })
        instance = super(UploadHistorySerializer, self).create(validated_data)
        self.load_file_upload(instance)
        return UploadTemporalService().get_temporal_summary(instance)

    def load_file_upload(self, instance):
        process_upload_tenporal.send(instance.id)


class UploadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHistory
        fields = ('status', )

    def update(self, instance, validated_data):
        instance = super(UploadStatusSerializer, self).update(instance, validated_data)
        if instance.status == 'IN_PROGRESS':
            process_upload_land.send(instance.id)

        return instance


class LandSerializer(serializers.ModelSerializer):
    has_owners = serializers.SerializerMethodField(read_only=True)
    has_applications  = serializers.SerializerMethodField()
    #has_lands_affected_applications = serializers.SerializerMethodField(read_only=True)
    applications = serializers.SerializerMethodField()
    #lands_affected_applications = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Land
        fields = '__all__'  # ToDo: estandarizar listado de predios

    def get_has_owners(self, obj):
        return LandOwnerDetail.objects.filter(land_id=obj.id).exists()

    def get_has_applications(self, obj):
        #ApplicationLandDetail.objects.filter(land_id=obj.id_lote_p).filter(application__id_status=1).exists()
        #return ApplicationLandDetail.objects.filter(land_id=obj.id).filter(application__id_status=1).exists()

        if obj.id_lote_p is not None and obj.id_lote_p !='':
            return ApplicationLandDetail.objects.filter(land__id_lote_p=obj.id_lote_p).filter(application__id_status=1).exists()
            
        else:
            return ApplicationLandDetail.objects.filter(land_id=obj.id).filter(application__id_status=1).exists()
        
    
    def get_applications(self, obj):
        respuesta = []
        if  obj.id_lote_p is not None and obj.id_lote_p !='':
            id_lands_affected=Land.objects.filter(id_lote_p=obj.id_lote_p).filter(status__in=[1,4]).values_list('id', flat=True)
            
            application_ids=ApplicationLandDetail.objects.filter(land_id__in=id_lands_affected).filter(application__id_status=1).values_list('application__id', flat=True)
            
            data_app=Application.objects.filter(id__in =application_ids)
            #print('data_app',data_app)
            if len(data_app)>0:
                serializer =ApplicationListSerializer(data_app[0], many = False)
                return serializer.data
            else:
                return None
        

        else:
            application_ids=ApplicationLandDetail.objects.filter(land_id=obj.id).filter(application__id_status=1).values_list('application__id', flat=True)
            data_app=Application.objects.filter(id__in =application_ids)
            if len(data_app)>0:

                serializer =ApplicationListSerializer(data_app[0], many = False)
                return serializer.data
            else:
                return None
        # data = ApplicationLandDetail.objects.filter(land_id=obj.id).filter(application__id_status=1)
        # serializer =ApplicationSerializer(data= data, many = True)
        # return serializer.data
    
    # def get_has_lands_affected_applications(self,obj):
    #     id_lands_affected=Land.objects.filter(id_lote_p=obj.id_lote_p).filter(status__in=[1,4]).exclude(id=obj.id).values_list('id', flat=True)

    #     return ApplicationLandDetail.objects.filter(land_id__in=id_lands_affected).filter(application__id_status=1).exists()



class LandSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'

    def create(self, validated_data):
        owner = validated_data.get('owner')
        ubigeo = validated_data.get('ubigeo')
        instance = super(LandSaveSerializer, self).create(validated_data)
        LandOwnerDetail.objects.create(owner=owner, land=instance, ubigeo=ubigeo)
        instance.owner.number_lands = LandOwnerDetail.objects.filter(owner=owner).count()
        instance.owner.save()
        return instance

    def update(self, instance, validated_data):
        instance = super(LandSaveSerializer, self).update(instance, validated_data)
        validated_data['id_reference'] = instance.id
        validated_data['created_by'] = 'admin'
        validated_data['update_by'] = 'admin'

        if 'id' in validated_data:
            del validated_data['id']

        validated_data['source_change'] = 'asignar_lote'
        validated_data['type'] = 'editar'
        LandAudit.objects.create(**validated_data)
        return instance


class LandOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandOwner
        fields = '__all__'


class OwnerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerAddress
        fields = '__all__'


class LandOwnerDetailSerializer(serializers.ModelSerializer):
    address = OwnerAddressSerializer(allow_null=True)

    class Meta:
        model = LandOwner
        fields = '__all__'
        
        
class LandOwnerDetailSRTMSerializer(serializers.ModelSerializer):

    class Meta:
        model = LandOwnerDetail
        fields = '__all__'
        
    def exists_detail(self, data):
        return LandOwnerDetail.objects.filter(owner=data.get('owner'), land=data.get('land'),ubigeo =data.get('ubigeo')).exists()

    @transaction.atomic
    def create(self, validated_data):
        #print('validated_data>>',validated_data)
        if self.exists_detail(data=validated_data) :

            raise serializers.ValidationError({'message':'Ya existe esta relacion entre predio y contribuyente'})

        detail = LandOwnerDetail.objects.create(**validated_data)


                
        return detail
    


class LandOwnerSaveSerializer(serializers.ModelSerializer):

    address = OwnerAddressSerializer(allow_null=True, write_only=True)

    class Meta:
        model = LandOwner
        fields = '__all__'

    def exists_owner(self, data):
        return LandOwner.objects.filter(ubigeo=data.get('ubigeo'), code=data.get('code')).exists()
        #return False
        #return LandOwner.objects.filter(document_type=data.get('document_type'), dni=data.get('dni')).exists()

    @transaction.atomic
    def create(self, validated_data):
        if self.exists_owner(data=validated_data) :
            raise serializers.ValidationError({'message':'Ya existe el contribuyente con el documento ingresado'})
        
        address = validated_data.pop('address')
        owner = LandOwner.objects.create(**validated_data)

        address.update({"owner": owner})
        OwnerAddress.objects.create(**address)
        return owner

    @transaction.atomic
    def update(self, instance, validated_data):
        nom_update_fiels = ['dni', 'document_type']
        address = {}
        if validated_data.get('address'):
            address = validated_data.pop('address')
        if set(nom_update_fiels).intersection(set(validated_data.keys())):
            raise serializers.ValidationError(f'Los campos {nom_update_fiels} no pueden ser modificados')
        instance = super(LandOwnerSaveSerializer, self).update(instance, validated_data)
        OwnerAddress.objects.filter(owner=instance).update(**address)
        return instance
    

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'




class LandOwnerSRTMSerializer(serializers.ModelSerializer):
    domicilios = DomicilioSerializer(many = True,allow_null=True)
    contactos = ContactoSerializer(many = True,allow_null=True)
    class Meta:
        model = LandOwner
        fields = '__all__'


    def exists_owner(self, data):
        return LandOwner.objects.filter(ubigeo=data.get('ubigeo'), code=data.get('code')).exists()

    @transaction.atomic
    def create(self, validated_data):
        #print('validated_data>>',validated_data)
        if self.exists_owner(data=validated_data) :
            raise serializers.ValidationError({'message':'Ya existe el contribuyente en este distrito','status':False}  )


        domicilios =validated_data.pop('domicilios')   if validated_data.get('domicilios') else []
        contactos =validated_data.pop('contactos')   if validated_data.get('contactos') else []
        owner = LandOwner.objects.create(**validated_data)

        for domicilio in domicilios:
            domicilio.update({"contribuyente": owner})
            Domicilio.objects.create(**domicilio)
        
        for contacto in contactos:
            contacto.update({"contribuyente": owner})
            Contacto.objects.create(**contacto)

        # if validated_data.get('domicilios'):
        #     domicilios = validated_data.pop('domicilios')
        #     print('domicilios>>',domicilios)

                
        return owner



class SummaryRecordSerializer(serializers.Serializer):
    total_records = serializers.IntegerField()
    mapping_records = serializers.IntegerField()
    without_mapping_records = serializers.IntegerField()
    inactive_records= serializers.IntegerField()

class TemporalUploadSummarySerializer(serializers.Serializer):
    upload_history_id = serializers.IntegerField()
    type_upload = serializers.CharField(default='TB_PREDIO')
    status = serializers.CharField()
    total = serializers.IntegerField()
    errors = serializers.IntegerField()
    corrects = serializers.IntegerField()
    new = serializers.IntegerField()
    updates = serializers.IntegerField()
    errors_data = serializers.SerializerMethodField()
    corrects_data = serializers.SerializerMethodField()

    def get_errors_data(self, obj):
        return list(obj.get('errors_data', []))

    def get_corrects_data(self, obj):
        return list(obj.get('corrects_data', []))


class LandDetailSerializer(serializers.ModelSerializer):

    owner = LandOwnerDetailSerializer()

    class Meta:
        model = Land
        fields = '__all__'


class LandNivelConstruccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandNivelConstruccion
        fields = '__all__'

    def exists_nivel(self, data):
        return LandNivelConstruccion.objects.filter(land_owner_detail=data.get('land_owner_detail'), num_piso=data.get('num_piso')).exists()
        #return False
        #return LandOwner.objects.filter(document_type=data.get('document_type'), dni=data.get('dni')).exists()

    @transaction.atomic
    def create(self, validated_data):
        if self.exists_nivel(data=validated_data) :
            raise serializers.ValidationError({'message':'Ya existe este nivel para el predio','status':False})
        
        detail = LandNivelConstruccion.objects.create(**validated_data)
        return detail

    

class OwnerDeudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerDeuda
        fields= '__all__'
    def exists_deuda(self, data):
        return OwnerDeuda.objects.filter(owner=data.get('owner'), anio=data.get('anio')).exists()


    @transaction.atomic
    def create(self, validated_data):
        if self.exists_deuda(data=validated_data) :
            raise serializers.ValidationError({'message':'Ya existe esta deuda para este contribuyente y con este año','status':False})
        
        detail = OwnerDeuda.objects.create(**validated_data)
        return detail