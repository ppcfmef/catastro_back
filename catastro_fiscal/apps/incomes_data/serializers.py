from rest_framework import serializers
from apps.lands.models import UploadHistory
from .services.rt_contribuyente_upload_temporal import RTContribuyenteUploadTemporalService


class IncomeUploadHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadHistory
        fields = ('id', 'file_upload', 'type_upload')

    def create(self, validated_data):
        username = getattr(self.context.get('request'), 'user', None)
        validated_data.update({
            'username': username
        })
        instance = super(IncomeUploadHistorySerializer, self).create(validated_data)
        upload_temporal_service = self.fabric_temporal_service(instance.type_upload)
        self.load_file_upload(upload_temporal_service, instance)
        return upload_temporal_service().get_temporal_summary(instance)

    def load_file_upload(self, upload_temporal_service, instance):
        upload_temporal_service().execute(instance)

    def fabric_temporal_service(self, type_upload):
        if type_upload == 'RT_CONTRIBUYENTE':
            return RTContribuyenteUploadTemporalService
        else:
            raise serializers.ValidationError('No existe tipo de carga para procesar')
