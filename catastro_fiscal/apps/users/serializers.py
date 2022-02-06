from rest_framework import serializers
from apps.master_data.serializers import InstitutionSerializer
from apps.places.serializers import DepartmentSerializer, ProvinceSerializer, DistrictSerializer
from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RoleShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class UserProfileShortSerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'name', 'email')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'institution', 'dni', 'first_name', 'last_name', 'email', 'job_title', 'role', 'username',
                  'password', 'is_active', 'department', 'province', 'district', 'observation')


class UserListSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()
    role = RoleShortSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'institution', 'role', 'is_active', 'date_joined')


class UserDetailSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()
    role = RoleShortSerializer()
    department = DepartmentSerializer()
    province = ProvinceSerializer()
    district = DistrictSerializer()

    class Meta:
        model = User
        exclude = ('is_staff', 'last_login', 'is_superuser', 'groups', 'user_permissions')
