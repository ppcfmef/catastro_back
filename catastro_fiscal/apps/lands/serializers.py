from django.db import transaction
from rest_framework import serializers, status
from rest_framework.response import Response
from .models import UploadHistory, Land, LandOwner, OwnerAddress, LandAudit
from .services.upload_temporal import UploadTemporalService


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
        return UploadTemporalService().get_temporal_summary(instance)

    def load_file_upload(self, instance):
        UploadTemporalService().execute(instance)


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

    def create(self, validated_data):
        instance = super(LandSaveSerializer, self).create(validated_data)
        instance.owner.number_lands = Land.objects.filter(owner=instance.owner).count()
        instance.owner.save()
        return instance

    def update(self, instance, validated_data):
        instance = super(LandSaveSerializer, self).update(instance, validated_data)
        validated_data['id_reference'] = instance.id
        validated_data['created_by'] = 'admin'
        validated_data['update_by'] = 'admin'

        if 'id' in validated_data:
            del validated_data['id']

        validated_data['source_change'] = 'asignar_lote'
        validated_data['type'] = 'editar'
        LandAudit.objects.create(**validated_data)
        return instance


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


class SummaryRecordSerializer(serializers.Serializer):
    total_records = serializers.IntegerField()
    mapping_records = serializers.IntegerField()
    without_mapping_records = serializers.IntegerField()


class TemporalUploadSummarySerializer(serializers.Serializer):
    total = serializers.IntegerField()
    erros = serializers.IntegerField()
    corrects = serializers.IntegerField()
    new = serializers.IntegerField()
    updates = serializers.IntegerField()
