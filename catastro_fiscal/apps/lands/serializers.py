from django.db import transaction
from rest_framework import serializers
from .models import UploadHistory, Land, LandOwner, OwnerAddress, LandAudit
from .services.upload_temporal import UploadTemporalService
from .services.upload_land import UploadLandService


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


class UploadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHistory
        fields = ('status', )

    def update(self, instance, validated_data):
        instance = super(UploadStatusSerializer, self).update(instance, validated_data)
        if instance.status == 'IN_PROGRESS':
            UploadLandService().execute(upload_history=instance)

        return instance


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'  # ToDo: estandarizar listado de predios


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

    def exists_owner(self, data):
        return LandOwner.objects.filter(document_type=data.get('document_type'), dni=data.get('dni')).exists()

    @transaction.atomic
    def create(self, validated_data):
        if self.exists_owner(data=validated_data) :
            raise serializers.ValidationError(f'Ya existe el contribuyente con el documento ingresado')
        address = validated_data.pop('address')
        owner = LandOwner.objects.create(**validated_data)

        address.update({"owner": owner})
        OwnerAddress.objects.create(**address)
        return owner

    @transaction.atomic
    def update(self, instance, validated_data):
        nom_update_fiels = ['dni', 'document_type']
        address = {}
        if validated_data.get('address'):
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
    upload_history_id = serializers.IntegerField()
    status = serializers.CharField()
    total = serializers.IntegerField()
    errors = serializers.IntegerField()
    corrects = serializers.IntegerField()
    new = serializers.IntegerField()
    updates = serializers.IntegerField()
    errors_data = serializers.SerializerMethodField()
    corrects_data = serializers.SerializerMethodField()

    def get_errors_data(self, obj):
        return list(obj.get('errors_data', []))

    def get_corrects_data(self, obj):
        return list(obj.get('corrects_data', []))


class LandDetailSerializer(serializers.ModelSerializer):

    owner = LandOwnerDetailSerializer()

    class Meta:
        model = Land
        fields = '__all__'
