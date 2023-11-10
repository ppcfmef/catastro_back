from datetime import timedelta
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings


api_settings.JWT_EXPIRATION_DELTA = timedelta(hours=48)


class MobileJWTSerializer(JSONWebTokenSerializer):

    def validate(self, data):
        auth_response = JSONWebTokenSerializer.validate(self, data)
        user = auth_response.get('user')
        if user:
            if user.is_superuser or user.is_mobile_staff:
                return auth_response
            raise serializers.ValidationError('No tiene permisos para ingresar a la aplicación móvil')


class GeneralResponseSerializer(serializers.Serializer):
    STATUS_CHOICES = (
        ('success', 'success'),
        ('error', 'error'),
    )
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    message = serializers.CharField()
