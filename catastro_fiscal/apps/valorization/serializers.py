from rest_framework import serializers, exceptions
from .models import (
    Photo,PhotoType
)

class PhotoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoType
        fields = '__all__'  # ToDo: estandarizar listado de predios


class PhotoSerializer(serializers.ModelSerializer):
    desc_tipo_foto =  serializers.CharField(source='cod_tipo_foto.desc_tipo_foto')
    class Meta:
        model = Photo
        fields = '__all__'  # ToDo: estandarizar listado de predios