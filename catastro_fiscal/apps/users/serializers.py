from rest_framework import serializers
from apps.master_data.serializers import InstitutionSerializer
from apps.places.serializers import DepartmentSerializer, ProvinceSerializer, DistrictSerializer
from .models import User, Role, Permission, PermissionNavigation, PermissionType


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

    def create(self, validated_data):
        permissions_navigation = validated_data.pop('permissions_navigation')
        instance = super(PermissionSerializer, self).create(validated_data)
        self.create_permissions_navigation(
            permission=instance,
            permissions_navigation=permissions_navigation
        )
        return instance

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
        PermissionNavigation.objects.exclude(id__in=permission_navigation_ids).delete()

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
