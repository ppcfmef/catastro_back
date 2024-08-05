from django.db import transaction
from apps.lands.models import LandOwnerDetail
from apps.lands.serializers import OwnerAddressSerializer
from rest_framework import serializers

#,AplicationType,

from apps.lands.models import Land,LandOwner
from apps.lands.serializers import LandOwnerRetriveSerializer
from apps.master_data.models import MasterCodeStreet
import django_filters
from django import forms


from apps.places.models import District
# class AplicationType(serializers.ModelSerializer):
#     class Meta:
#         model = AplicationType
#         fields = '__all__'



    
class LandListAnalisysSerializer(serializers.ModelSerializer):
    
    district = serializers.CharField(source='ubigeo.name')
    province = serializers.CharField(source='ubigeo.province.name')
    department = serializers.CharField(source='ubigeo.province.department.name')
    #street_type_name = serializers.SerializerMethodField()
    street_type_name= serializers.CharField(source='street_type.name',read_only=True)
    owner_name = serializers.SerializerMethodField()
    #description_owner = serializers.CharField(source='owner.description_owner')
    #owner = LandOwnerDetailSerializer()
    class Meta:
        model = Land
        fields = '__all__'  # ToDo: estandarizar listado de predios
        


    # def get_street_type_name(self,obj):
    #     try:
    #         street=MasterCodeStreet.objects.get(id= obj.street_type)
    #         return street.name
    #     except MasterCodeStreet.DoesNotExist:
    #         return ''
            
        
    def get_owner_name(self, obj):
        landOwner=LandOwnerDetail.objects.filter(land_id=obj.id)
        if len(landOwner)>0:
            return '{} {} {}'.format(landOwner[0].owner.name  if landOwner[0].owner.name else '' ,landOwner[0].owner.paternal_surname  if landOwner[0].owner.paternal_surname else '',landOwner[0].owner.maternal_surname  if landOwner[0].owner.maternal_surname else '') 
        else:
            return None
        #return LandOwnerDetail.objects.filter(land_id=obj.id)
        
class LandOwnerAnalisysSerializer(serializers.ModelSerializer):
    address = OwnerAddressSerializer(allow_null=True)
    class Meta:
        model = LandOwner
        fields = '__all__'
    
class LandAnalisysSerializer(serializers.ModelSerializer):
    #owner = LandOwnerDetailSerializer()
    land_owner = serializers.SerializerMethodField()
    street_type_name= serializers.CharField(source='street_type.name',read_only=True)
    class Meta:
        model = Land
        fields = '__all__'
    
    def get_land_owner(self, obj):
        query=LandOwnerDetail.objects.filter(land_id=obj.id)
        owner=None
        #for q in query:
            #owners.append(q.owner)
        if len(query)>0:
            owner=query[0].owner
        serializer = LandOwnerAnalisysSerializer(owner, many=False)
        #serializer = self.get_serializer(queryset, many=True)
        return serializer.data
    
        
class DistrictAnalisysSerializer(serializers.ModelSerializer):
    
    district_name = serializers.CharField(source='name')
    province_name = serializers.CharField(source='province.name')
    department_name = serializers.CharField(source='province.department.name')
    class Meta:
        model = District
        fields = ('code',  'district_name', 'province_name','department_name')
    

