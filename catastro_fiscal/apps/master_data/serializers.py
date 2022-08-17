from rest_framework import serializers
from .models import (
    Institution, MasterTypeUrbanUnit, MasterSide, MasterCodeStreet, MasterPropertyType
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


class MasterDomainSerilizer(serializers.Serializer):
    uu_type = MasterTypeUrbanUnitSerializer(many=True)
    cod_street = MasterCodeStreetSerializer(many=True)
    property_type = MasterPropertyTypeSerializer(many=True)
    cod_side = MasterSideSerializer(many=True)

    def get_uu_type(self, obj):
        return MasterTypeUrbanUnit.objects.all()

    def get_cod_street(self, obj):
        return MasterCodeStreet.objects.all()

    def get_property_type(self, obj):
        return MasterPropertyType.objects.all()

    def get_cod_side(self, obj):
        return MasterSide.objects.all()
