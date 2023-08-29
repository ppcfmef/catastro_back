from rest_framework import serializers
from apps.lands.models import UploadHistory
from .services.rt_contribuyente_upload_temporal import RTContribuyenteUploadTemporalService
from .services.rt_marcopredio_upload_temporal import RTMarcoPredioUploadTemporalService
from .services.rt_arancel_upload_temporal import RTArancelUploadTemporalService
from .tasks import process_incomes_upload_tenporal, process_incomes_upload
from .models import (
    Contribuyente, MarcoPredio, Arancel, PredioDato, PredioCaracteristica, Recaudacion, Deuda, Emision, BaseImponible,
    Alicuota, AmnistiaContribuyente, AmnistiaMunicipal, VaremMunicipal
)


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
        self.load_file_upload(instance)
        return upload_temporal_service().get_temporal_summary(instance)

    def load_file_upload(self, instance):
        process_incomes_upload_tenporal.send(instance.id)

    def fabric_temporal_service(self, type_upload):
        if type_upload == 'RT_CONTRIBUYENTE':
            return RTContribuyenteUploadTemporalService
        elif type_upload == 'RT_MARCO_PREDIO':
            return RTMarcoPredioUploadTemporalService
        elif type_upload == 'RT_ARANCEL':
            return RTArancelUploadTemporalService
        else:
            raise serializers.ValidationError('No existe tipo de carga para procesar')


class IncomeUploadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHistory
        fields = ('status', )

    def update(self, instance, validated_data):
        instance = super(IncomeUploadStatusSerializer, self).update(instance, validated_data)
        if instance.status == 'IN_PROGRESS':
            process_incomes_upload.send(instance.id)
        return instance


class RTContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuyente
        fields = '__all__'


class RTMarcoPredioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcoPredio
        fields = '__all__'


class RTArancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arancel
        fields = '__all__'


class RTPredioDatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredioDato
        fields = '__all__'


class RTPredioCaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredioCaracteristica
        fields = '__all__'


class RTRecaudacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recaudacion
        fields = '__all__'


class RTDeudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deuda
        fields = '__all__'


class RTEmisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emision
        fields = '__all__'


class RTBaseImponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseImponible
        fields = '__all__'


class RTAlicuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alicuota
        fields = '__all__'


class RTAmnistiaContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmnistiaContribuyente
        fields = '__all__'


class RTAmnistiaMunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmnistiaMunicipal
        fields = '__all__'


class RTVaremMunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaremMunicipal
        fields = '__all__'
