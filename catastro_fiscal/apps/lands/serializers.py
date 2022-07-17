from django.db import transaction
from rest_framework import serializers
from .models import UploadHistory, Land, LandOwner, OwnerAddress
from .services import UploadLandRecordService


class UploadHistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHistory
        fields = '__all__'


class UploadHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHistory
        fields = ('id', 'file_upload',)

    def create(self, validated_data):
        username = getattr(self.context.get('request'), 'user', None)
        validated_data.update({
            'username': username
        })
        instance = super(UploadHistorySerializer, self).create(validated_data)
        self.load_file_upload(instance)
        return instance

    def load_file_upload(self, instance):
        UploadLandRecordService().execute(instance)


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'  # ToDo: estandarizar listado de predios


class LandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'


class LandSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'


class LandOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandOwner
        fields = '__all__'


class OwnerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerAddress
        fields = '__all__'


class LandOwnerDetailSerializer(serializers.ModelSerializer):
    address = OwnerAddressSerializer(allow_null=True)

    class Meta:
        model = LandOwner
        fields = '__all__'


class LandOwnerSaveSerializer(serializers.ModelSerializer):

    address = OwnerAddressSerializer(allow_null=True, write_only=True)

    class Meta:
        model = LandOwner
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        address = validated_data.pop('address')
        owner = LandOwner.objects.create(**validated_data)
        address.update({"owner": owner})
        OwnerAddress.objects.create(**address)
        return owner

    @transaction.atomic
    def update(self, instance, validated_data):
        nom_update_fiels = ['dni', 'document_type']
        address = validated_data.pop('address')
        if set(nom_update_fiels).intersection(set(validated_data.keys())):
            raise serializers.ValidationError(f'Los campos {nom_update_fiels} no pueden ser modificados')
        instance = super(LandOwnerSaveSerializer, self).update(instance, validated_data)
        OwnerAddress.objects.filter(owner=instance).update(**address)
        return instance
