from django.db import transaction
from rest_framework import serializers
from .models import  Result,Application,ApplicationObservationDetail,ApplicationLandDetail,ApplicationResultDetail
#,AplicationType,

from apps.lands.models import Land
from apps.master_data.models import MasterCodeStreet
import django_filters
from django import forms
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
    class Meta:
        model = Application
        fields = '__all__'

    def get_lands(self, obj):
        lands_id=ApplicationLandDetail.objects.filter(application_id=obj.id).values_list('land_id', flat=True)
        return  list(Land.objects.filter(id__in=list(lands_id)).values('cpm'))
    
    def get_status(self,obj):
        return obj.get_id_status_display()
    
    def get_type(self,obj):
        return obj.get_id_type_display()


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



    
class LandListSerializer(serializers.ModelSerializer):
    has_applications = serializers.SerializerMethodField()
    district = serializers.CharField(source='ubigeo.name')
    province = serializers.CharField(source='ubigeo.province.name')
    department = serializers.CharField(source='ubigeo.province.department.name')
    street_type_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Land
        fields = '__all__'  # ToDo: estandarizar listado de predios
        
    def get_has_applications(self, obj):
        return ApplicationLandDetail.objects.filter(land_id=obj.id).exists()
    
    def get_street_type_name(self,obj):
        try:
            street=MasterCodeStreet.objects.get(id= obj.street_type)
            return street.name
        except MasterCodeStreet.DoesNotExist:
            return ''
            
        
        
    
    
class LandByApplicationListSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Land
        fields = ('cpm','cup','cod_cuc','street_name_alt','street_name','sec_ejec',) 
        
    
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
    
    class Meta:
        model = Result
        fields = ('address','cpm','urban_lot_number')
        
    def get_address(self,obj):
        street_type=MasterCodeStreet.objects.get(id= obj.street_type)
        return '{} {} {}'.format(street_type.name,obj.street_name,obj.municipal_number)