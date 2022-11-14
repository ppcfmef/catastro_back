from django.db import transaction
from rest_framework import serializers
from apps.master_data.serializers import InstitutionSerializer
from apps.places.serializers import (
    DepartmentSerializer, ProvinceSerializer, DistrictSerializer, PlaceScopeSerializer
)
from .models import User, Role, Permission, PermissionNavigation, PermissionType, RolePermission

from rest_captcha.serializers import RestCaptchaSerializer

class RoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True)

    class Meta:
        model = Role
        fields = '__all__'

    def create(self, validated_data):
        permissions = validated_data.pop('permissions')
        instance = super(RoleSerializer, self).create(validated_data)
        instance.permissions.add(*permissions)
        return instance

    def update(self, instance, validated_data):
        permissions = validated_data.pop('permissions')
        instance = super(RoleSerializer, self).update(instance, validated_data)
        permissions_ids = []
        for permission in permissions:
            obj, create = RolePermission.objects.get_or_create(
                role=instance,
                permission=permission
            )
            permissions_ids.append(obj.pk)
        RolePermission.objects.exclude(id__in=permissions_ids).delete()
        return instance


class RoleShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class UserProfileShortSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    place_scope = PlaceScopeSerializer()
    permissions_navigation = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'avatar', 'email', 'place_scope', 'ubigeo', 'permissions_navigation')

    def get_permissions_navigation(self, obj):
        permissions = RolePermission.objects.filter(role=obj.role).values_list('permission', flat=True)
        permission_navigation = PermissionNavigation.objects.filter(permission__in=permissions)
        return PermissionNavigationSerializer(permission_navigation, many=True).data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'institution', 'avatar', 'dni', 'first_name', 'last_name', 'email', 'job_title', 'role',
                  'username', 'password', 'is_active', 'department', 'province', 'district', 'observation',
                  'place_scope')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('username', None)  # ToDo: El usuario no se edita
        password = validated_data.pop('password', None)
        instance = super(UserSerializer, self).update(instance, validated_data)
        if password:
            instance.set_password(password)
        return instance


class UserListSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()
    role = RoleShortSerializer()

    class Meta:
        model = User
        fields = ('id', 'dni', 'username', 'institution', 'district', 'role', 'is_active', 'date_joined')


class UserDetailSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()
    role = RoleShortSerializer()
    department = DepartmentSerializer()
    province = ProvinceSerializer()
    district = DistrictSerializer()
    place_scope = PlaceScopeSerializer()

    class Meta:
        model = User
        exclude = ('is_staff', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'password')


class PermissionNavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionNavigation
        fields = ('id', 'type', 'navigation_view')


class PermissionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'description')


class PermissionSerializer(serializers.ModelSerializer):
    permissions_navigation = PermissionNavigationSerializer(many=True, allow_null=True)

    class Meta:
        model = Permission
        fields = ('id', 'description', 'permissions_navigation')

    @transaction.atomic
    def create(self, validated_data):
        permissions_navigation = validated_data.pop('permissions_navigation')
        # Creamos el permiso y Rol con los mismos datos y la relacion entre ambos
        instance = super(PermissionSerializer, self).create(validated_data)  # permiso
        role = Role.objects.create(name=validated_data.get('description'))  # Rol
        role.permissions.add(instance)  # Rol/Permiso

        # Agregando permisos de navegacion
        self.create_permissions_navigation(
            permission=instance,
            permissions_navigation=permissions_navigation
        )
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        permissions_navigation = validated_data.pop('permissions_navigation')
        instance = super(PermissionSerializer, self).update(instance, validated_data)
        self.update_permissions_navigation(
            permission=instance,
            permissions_navigation=permissions_navigation
        )
        return instance

    def create_permissions_navigation(self, permission, permissions_navigation):
        permissions_navigation_bulk = []
        for permission_navigation in permissions_navigation:
            permissions_navigation_data = self.get_permissions_navigation_data(
                permission,
                permission_navigation=dict(permission_navigation)
            )
            permissions_navigation_bulk.append(PermissionNavigation(**permissions_navigation_data))

        # create all records
        PermissionNavigation.objects.bulk_create(permissions_navigation_bulk)

    def update_permissions_navigation(self, permission, permissions_navigation):
        permission_navigation_ids = []
        for permission_navigation in permissions_navigation:
            permission_navigation = dict(permission_navigation)
            permissions_navigation_data = self.get_permissions_navigation_data(
                permission,
                permission_navigation=dict(permission_navigation)
            )

            obj, create = PermissionNavigation.objects.get_or_create(**permissions_navigation_data)
            permission_navigation_ids.append(obj.pk)

        # deleting records not sent in permissions_navigation
        PermissionNavigation.objects.filter(permission=permission).exclude(id__in=permission_navigation_ids).delete()

    def get_permissions_navigation_data(self, permission, permission_navigation):
        return {
            'permission': permission,
            'type': permission_navigation.get('type'),
            'navigation_view': permission_navigation.get('navigation_view')
        }


class PermissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionType
        fields = ('code', 'description')
