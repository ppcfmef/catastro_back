from rest_framework import serializers
from .models import Department, Province, District, PlaceScope, Extension, Resource


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('code', 'name')


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('code', 'name', 'department')


class DistrictSerializer(serializers.ModelSerializer):
    department = serializers.CharField()

    class Meta:
        model = District
        fields = ('code', 'name', 'department', 'province')


class PlaceScopeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaceScope
        fields = ('id', 'name')


class ExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extension
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class DistrictResourceSerializer(serializers.ModelSerializer):
    department = serializers.CharField()
    extensions = ExtensionSerializer(many=True)
    resources = ResourceSerializer(many=True)

    class Meta:
        model = District
        fields = ('code', 'name', 'department', 'province', 'extensions', 'resources','municipal_name')
