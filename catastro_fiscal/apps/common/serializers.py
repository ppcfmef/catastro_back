from rest_framework import serializers
from .models import Navigation


class NavigationSerializer(serializers.ModelSerializer):
    full_title = serializers.CharField(read_only=True)

    class Meta:
        model = Navigation
        fields = '__all__'


class NavigationTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Navigation
        fields = ('id', 'title', 'subtitle', 'type', 'icon', 'link', 'order')

    def to_representation(self, obj):
        if 'children' in obj:
            self.fields['children'] = NavigationTreeSerializer(obj, many=True)
        return super(NavigationTreeSerializer, self).to_representation(obj)


class NavigationAuthorizationSerializer(serializers.Serializer):
    id = serializers.CharField()
    permission_type = serializers.CharField()

    def validate(self, attrs):
        user = getattr(self.context["request"], "user", None)
        if user is None:
            raise serializers.ValidationError('No existe el usuario')

        if user.is_superuser:
            return attrs
        elif self.validate_navigation_authorization(user.role, attrs):
            return attrs
        else:
            raise serializers.ValidationError('No tiene permisos para acceder a esta pagina')

    def validate_navigation_authorization(self, role, attrs):
        navigation_id = attrs.get('id', None)
        permission_type = attrs.get('permission_type', None)

        if role is None or id is None or permission_type is None:
            return False

        permission = role.permission
        if permission is None:
            return False

        permission_navigation = permission.permissions.filter(
            navigation_view_id=navigation_id,
            type__code__startswith=permission_type
        )
        return permission_navigation.exists()
