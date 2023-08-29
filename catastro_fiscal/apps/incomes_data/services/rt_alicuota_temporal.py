from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import Alicuota


class AlicuotaValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alicuota
        fields = '__all__'


class RTAlicuotaUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = AlicuotaValidSerializer

    def mapper(self):
        return {
            "ano_ejec": "ano_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "cod_contr": "cod_contr",
            "rec_pred_alicuota": "rec_pred_alicuota",
            "emision_pred_alicuota": "emision_pred_alicuota",
            "fecha_data": "fecha_data",
        }
