from rest_framework import serializers
from .models import (
    Institution, MasterTypeUrbanUnit, MasterSide, MasterCodeStreet, MasterPropertyType, MasterResolutionType,ResolutionTypeDistrito
)


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('id', 'name')


class MasterTypeUrbanUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterTypeUrbanUnit
        fields = '__all__'


class MasterCodeStreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCodeStreet
        fields = '__all__'


class MasterPropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterPropertyType
        fields = '__all__'


class MasterSideSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterSide
        fields = '__all__'


class MasterResolutionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterResolutionType
        fields = '__all__'


class ResolutionTypeDistritoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResolutionTypeDistrito
        fields = '__all__'


class ResolutionTypeDistritoSerializer(serializers.ModelSerializer):
    
    id = serializers.CharField(source='resolucion.id')

    class Meta:
        model = ResolutionTypeDistrito
        fields = '__all__'



# class ResolutionTypeDistritoSerializerList(serializers.ModelSerializer):
#     id_resolucion = serializers.CharField(source='resolucion.id')
#     name = serializers.CharField(source='resolucion.name')
#     description = serializers.CharField(source='resolucion.description')
#     short_name = serializers.CharField(source='resolucion.short_name')
#     class Meta:
#         model = ResolutionTypeDistrito
#         fields = ('id','id_resolucion','name','description','short_name','estado_registro','estado_mantenimiento')

class MasterDomainSerilizer(serializers.Serializer):
    uu_type = MasterTypeUrbanUnitSerializer(many=True)
    cod_street = MasterCodeStreetSerializer(many=True)
    property_type = MasterPropertyTypeSerializer(many=True)
    cod_side = MasterSideSerializer(many=True)
    resolution_type = MasterResolutionTypeSerializer(many=True)

    def get_uu_type(self, obj):
        return MasterTypeUrbanUnit.objects.all()

    def get_cod_street(self, obj):
        return MasterCodeStreet.objects.all()

    def get_property_type(self, obj):
        return MasterPropertyType.objects.all()

    def get_cod_side(self, obj):
        return MasterSide.objects.all()
