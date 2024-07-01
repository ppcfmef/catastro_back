from django.db import transaction
from rest_framework import serializers
from .models import UploadHistory, Land, LandOwner, OwnerAddress, LandAudit, LandOwnerDetail , Domicilio, Contacto , LandNivelConstruccion,OwnerDeuda
from apps.maintenance.models import ApplicationLandDetail , Application
from .tasks import process_upload_tenporal, process_upload_land
from .services.upload_temporal import UploadTemporalService
from .services.upload_land import UploadLandService
from rest_framework.response import Response
from apps.maintenance.serializers import ApplicationSerializer,ApplicationListSerializer
from rest_framework import  status
import json

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
        




class LandDetailSRTMSerializer(serializers.Serializer):

    ubigeo_predio =  serializers.CharField()
    municipalidad_id =  serializers.IntegerField(allow_null=True)
    
    codigo_predio_unico =  serializers.CharField()
    area_terreno = serializers.FloatField(allow_null=True)
    area_tot_terr_comun = serializers.FloatField(allow_null=True)
    area_construida = serializers.FloatField(allow_null=True)
    area_tot_cons_comun = serializers.FloatField(allow_null=True)
    por_propiedad = serializers.FloatField(allow_null=True)
    tip_transferencia_id = serializers.IntegerField(allow_null=True)
    tip_uso_predio_id= serializers.IntegerField(allow_null=True)
    tip_propiedad_id = serializers.IntegerField(allow_null=True)
    fec_transferencia = serializers.CharField(allow_null=True)
    longitud_frente = serializers.FloatField(allow_null=True)
    cantidad_habitantes = serializers.IntegerField(allow_null=True)
    pre_inhabitable = serializers.IntegerField(allow_null=True)
    par_registral  =  serializers.CharField(allow_null=True)
    numero_dj  =  serializers.CharField(allow_null=True)
    fecha_dj = serializers.CharField(allow_null=True)
    usuario_auditoria =  serializers.CharField(allow_null=True)
    estado_dj_id = serializers.IntegerField(allow_null=True)
    motivo_dj_id = serializers.IntegerField(allow_null=True)
    anio_determinacion = serializers.IntegerField(allow_null=True,required= False)
    longitud_frente =  serializers.FloatField(allow_null=True,required= False)
    class Meta:
        #model = LandOwnerDetail
        fields = '__all__'
        


    
class LandOwnerDetailSRTMSerializer(serializers.Serializer):
    contribuyente_numero =  serializers.CharField()
    predios = LandDetailSRTMSerializer(many=True,)
    class Meta:
        
        fields = '__all__'
    def exists_detail(self, data):
        return LandOwnerDetail.objects.filter(owner=data.get('owner'), land=data.get('land'),ubigeo =data.get('ubigeo')).exists()
    
    def create_detail(self, record):
        code_owner = record.get('contribuyente_numero',None)
        cpu = record.get('codigo_predio_unico',None)
        cpm = record.get('codigo_predio_municipal',None)
        ubigeo = record.get('ubigeo_predio')
       
        data = {
                'sec_ejec' :record.get('municipalidad_id',None),

                'cup' : record.get('codigo_predio_unico',None),
                'cpm' : record.get('codigo_predio_municipal',None),
                'ubigeo_id' : record.get('ubigeo_predio',None),
                'area_terreno':record.get('area_terreno',None),
                'area_tot_terr_comun': record.get('area_tot_terr_comun',None),
                'area_construida': record.get('area_construida',None),
                'area_tot_cons_comun': record.get('area_tot_cons_comun',None),
                'por_propiedad': record.get('por_propiedad',None),
                'tip_transferencia_id': record.get('tip_transferencia_id',None),
                'tip_uso_predio_id': record.get('tip_uso_predio_id',None),
                'tip_propiedad_id': record.get('tip_propiedad_id',None),
                'fec_transferencia': record.get('fec_transferencia',None),
                'longitud_frente': record.get('longitud_frente',None),
                'cantidad_habitantes': record.get('cantidad_habitantes',None),
                'pre_inhabitable': record.get('pre_inhabitable',None),
                'par_registral': record.get('par_registral',None),
                'numero_dj': record.get('numero_dj',None),
                'fecha_dj': record.get('fecha_dj',None),
                'usuario_auditoria': record.get('usuario_auditoria',None),
                'estado_dj': record.get('estado_dj_id',None),
                'motivo_dj': record.get('motivo_dj_id',None),
                'anio_determinacion':record.get('anio_determinacion',None),
               
            }
        
        
        owners=LandOwner.objects.filter(code =code_owner,ubigeo = ubigeo)
        lands=Land.objects.filter(cup =cpu,ubigeo = ubigeo)    

        if len(owners)==0:
            raise serializers.ValidationError({'message':'No existe el contribuyente','status':False})
        
        if len(lands)==0:
            raise serializers.ValidationError({'message':'No existe el predio','status':False})
        
        owner = owners[0]
        land = lands[0]


        
        data.update({'land_id':land.id,'owner_id': owner.id})
       
            
        if self.exists_detail(data=data):
            landOwnerDetails=LandOwnerDetail.objects.filter(owner=data.get('owner'), land=data.get('land'),ubigeo =data.get('ubigeo'))
            landOwnerDetails.update(estado_dj=3)
        detail = LandOwnerDetail.objects.create(**data)
        return detail
    

    @transaction.atomic
    def create(self, validate_data):
        predios=validate_data.pop('predios')
        for predio in predios:


            json_data = json.loads(json.dumps(predio))
            

            json_data['contribuyente_numero']=validate_data.get('contribuyente_numero')

            serializer_predio=self.create_detail(json_data)

        return True


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
        fields = ('descripcion','principal','tipo_med_contacto')

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = ('ubigeo_domicilio','tipo_domicilio','des_domicilio','latitud','longitud','referencia')

class MessageSerializer(serializers.Serializer):
    message=serializers.CharField()
    status = serializers.BooleanField()

class LandOwnerSRTMSerializer(serializers.Serializer):
    ubigeo_registro=serializers.CharField()
    municipalidad_id  = serializers.IntegerField()
    contribuyente_numero  = serializers.CharField()
    doc_identidad_id  = serializers.IntegerField()
    tip_contribuyente_id = serializers.IntegerField()
    num_doc_identidad = serializers.CharField()
    nombres = serializers.CharField(allow_null=True,allow_blank=True)
    ape_paterno = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    ape_materno = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    razon_social = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    domicilios = DomicilioSerializer(many = True,allow_null=True)
    contactos = ContactoSerializer(many = True,allow_null=True)

    class Meta:
        #model = LandOwner
        fields = '__all__'


    def exists_owner(self, data):
        return LandOwner.objects.filter(ubigeo=data.get('ubigeo_registro'), code=data.get('contribuyente_numero')).exists()

    @transaction.atomic
    def create(self, validated_data):
        document_type= validated_data.get('doc_identidad_id',None)
        document_type = '01' if document_type ==1 else '06' if document_type ==2 else   document_type 

        data = {
            'sec_ejec':validated_data.get('municipalidad_id',None), 
            'code' : validated_data.get('contribuyente_numero',None),
            'ubigeo_id' : validated_data.get('ubigeo_registro',None),
            'tipo_contribuyente_id':  validated_data.get('tip_contribuyente_id',None),
            'document_type_id' : document_type,
            'dni':validated_data.get('num_doc_identidad',None),
            'name': validated_data.get('nombres',None) if document_type == '01' else validated_data.get('razon_social',None)    ,
            'paternal_surname': validated_data.get('ape_paterno',None),
            'maternal_surname': validated_data.get('ape_materno',None),
            #'domicilios': validated_data.get('domicilios',[]),
            #'contactos': validated_data.get('contactos',[]),
        }


        if self.exists_owner(data=validated_data) :
            print('existe')
            owner = LandOwner.objects.filter(ubigeo=data.get('ubigeo_id'), code=data.get('code'))[0]
            

            for key, value in data.items():
                setattr(owner, key, value)
            owner.save()

            Domicilio.objects.filter(contribuyente_id = owner.id).delete()
            Contacto.objects.filter(contribuyente_id = owner.id).delete()

            domicilios =validated_data.pop('domicilios')   if validated_data.get('domicilios') else []
            contactos =validated_data.pop('contactos')   if validated_data.get('contactos') else []


            for domicilio in domicilios:
                domicilio.update({"contribuyente": owner})
                Domicilio.objects.create(**domicilio)
            
            for contacto in contactos:
                contacto.update({"contribuyente": owner})
                Contacto.objects.create(**contacto)

            return owner

            #print('contribuyente creado')
            #raise serializers.ValidationError({'message':'Contribuyente actualizado','status':True})

            #return Response({'message':'Contribuyente actualizado','status':True}, status=status.HTTP_200_OK  )
            #raise owner


            #raise serializers.va({'message':'Ya existe el contribuyente en este distrito','status':False}  )

            #raise serializers.ValidationError({'message':'Ya existe el contribuyente en este distrito','status':False}  )


        else:
            #print('no existe')
            domicilios =validated_data.pop('domicilios')   if validated_data.get('domicilios') else []
            contactos =validated_data.pop('contactos')   if validated_data.get('contactos') else []
            owner = LandOwner.objects.create(**data)

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