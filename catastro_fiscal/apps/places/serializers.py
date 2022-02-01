from rest_framework import serializers
from .models import Department, Province, District


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
