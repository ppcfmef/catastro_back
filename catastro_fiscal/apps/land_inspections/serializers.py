from django.db import transaction
from rest_framework import serializers
from .models import  Ticket,TicketSendStation,LandOwnerInspection,Location,LocationPhoto,LandFacility,SupplyType,LandSupply,LandFacility,LandInspectionType,RecordOwnerShip,LandCharacteristic,LandInspection



class LandSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = LandSupply
        fields = '__all__'

class LandInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandInspection
        fields = '__all__'  

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

class RecordOwnerShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordOwnerShip
        fields = '__all__' 


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'  

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'  


        

