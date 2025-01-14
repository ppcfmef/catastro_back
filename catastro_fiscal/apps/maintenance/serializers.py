from django.db import transaction
from rest_framework import serializers
from .models import  Result,Application,ApplicationObservationDetail,ApplicationLandDetail,ApplicationResultDetail
#,AplicationType,

from apps.lands.models import Land
from apps.master_data.models import MasterCodeStreet,MasterResolutionType
import django_filters
from django import forms

from core.utils.formato import Format
# class AplicationType(serializers.ModelSerializer):
#     class Meta:
#         model = AplicationType
#         fields = '__all__'



#class ApplicationObservationDetailForm(forms.ModelForm):
class ApplicationObservationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationObservationDetail
        fields = '__all__'


class ApplicationListSerializer(serializers.ModelSerializer):
    
    lands = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    #lands_affected = serializers.SerializerMethodField()
    class Meta:
        model = Application
        fields = '__all__'

    def get_lands(self, obj):
        lands_id=ApplicationLandDetail.objects.filter(application_id=obj.id).values_list('land_id', flat=True)
        return  list(Land.objects.filter(id__in=list(lands_id)).values('cpm','cup'))
    
    def get_status(self,obj):
        return obj.get_id_status_display()
    
    def get_type(self,obj):
        return obj.get_id_type_display()

    # def get_lands_affected(self,obj):

    #     lands_id=ApplicationLandDetail.objects.filter(application_id=obj.id).values_list('land_id', flat=True)
    #     id_plotes=list(Land.objects.filter(id__in=list(lands_id)).values_list('id_plot'))
    #     return Land.objects.filter(id_plot__in=list(id_plotes))

        #list(Land.objects.filter(id__in=list(lands_id)).values('cpm','cup'))


# class ApplicationStatusSerializer(serializers.ModelSerializer):
    
    
#     status = serializers.SerializerMethodField()
#     class Meta:
#         model = Application
#         fields = ('id','id_status','status')


#     def get_status(self,obj):
#         return obj.get_id_status_display()
class ApplicationSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Application
        fields = '__all__'


class LandAffectedSerializer(serializers.ModelSerializer):
    # district = serializers.CharField(source='ubigeo.name')
    # province = serializers.CharField(source='ubigeo.province.name')
    # department = serializers.CharField(source='ubigeo.province.department.name')
    
    class Meta:
        model = Land
        fields =('cpm','cup','cod_cuc','street_type','street_name_alt','street_name','sec_ejec','urban_lot_number','urban_mza','municipal_number','id_lote_p', 'creation_date') 
    
    
class LandListSerializer(serializers.ModelSerializer):
    has_applications = serializers.SerializerMethodField()
    district = serializers.CharField(source='ubigeo.name')
    province = serializers.CharField(source='ubigeo.province.name')
    department = serializers.CharField(source='ubigeo.province.department.name')
    #street_type_name = serializers.SerializerMethodField()
    street_type_name= serializers.CharField(source='street_type.name',read_only=True)
    lands_affected = serializers.SerializerMethodField()
    class Meta:
        model = Land
        fields = '__all__'  # ToDo: estandarizar listado de predios
        
    def get_has_applications(self, obj):
  
        return ApplicationLandDetail.objects.filter(land_id=obj.id).filter(application__id_status=1).exists()
    
    def get_lands_affected(self,obj):
        

        if obj.id_lote_p is not None and obj.id_lote_p !='': 
            queryset = Land.objects.filter(id_lote_p=obj.id_lote_p, ubigeo = obj.ubigeo ).filter(status__in=[1,4]).exclude(id=obj.id)
            serializer=LandAffectedSerializer(queryset,many= True)

            return serializer.data
        else:
            return []
            #lands_id=Land.objects.filter(land_id=obj.id).values_list('land_id', flat=True)


    
    # def get_street_type_name(self,obj):
    #     try:
    #         street=MasterCodeStreet.objects.get(id= obj.street_type)
    #         return street.name
    #     except MasterCodeStreet.DoesNotExist:
    #         return ''
            
        
        
    
    
class LandByApplicationListSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    
    class Meta:
        model = Land
        fields = ('cpm','cup','cod_cuc','street_type','street_name_alt','street_name','sec_ejec','urban_lot_number','urban_mza','municipal_number','address') 
    
    def get_address(self,obj):
        #print('obj.street_type>>',obj.street_type)
        #street_type=MasterCodeStreet.objects.get(id= obj.street_type)
        return '{street_type} {street_name} {municipal_number} {urban_mza} {urban_lot_number}'.format(street_type=obj.street_type.name,street_name = obj.street_name,municipal_number =obj.municipal_number,urban_mza ='Mz.{}'.format(obj.urban_mza) if Format.isNoneOrBlank(obj.urban_mza) else '' ,urban_lot_number ='Lote {}'.format( obj.urban_lot_number) if Format.isNoneOrBlank(obj.urban_lot_number)  else '' )


     
    
class LandApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'  

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'  


class ResultDetailCustomSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    resolution_type_name = serializers.SerializerMethodField()

    class Meta:
        model = Result
        fields = ('id','address','cpm','urban_lot_number','block','municipal_number','indoor','floor','km','municipal_address','cup','resolution_type','resolution_type_name','resolution_document')
        
    def get_address(self,obj):
        street_type=MasterCodeStreet.objects.get(id= obj.street_type)
        return """{street_type} {street_name} {municipal_number} {urban_mza} {urban_lot_number}""".format(street_type=street_type,street_name = obj.street_name, municipal_number =obj.municipal_number if Format.isNoneOrBlank(obj.municipal_number) else '' ,urban_mza ='Mz.{}'.format(obj.urban_mza) if Format.isNoneOrBlank(obj.urban_mza) else '', 
                                                                                                        urban_lot_number ='Lote {}'.format( obj.urban_lot_number) if  Format.isNoneOrBlank(obj.urban_lot_number) else '')

                                                                                                        
                                                                                                        
    
    def get_resolution_type_name(self,obj):
        try:
            resolution=MasterResolutionType.objects.get(id= obj.resolution_type)
            return resolution.name
        except MasterResolutionType.DoesNotExist:
            return ''