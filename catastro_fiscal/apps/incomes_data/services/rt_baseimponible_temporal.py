from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import BaseImponible


class BaseImponibleValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseImponible
        fields = '__all__'


class RTBaseImponibleUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = BaseImponibleValidSerializer

    def mapper(self):
        return {
            "ano_ejec": "ano_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "cod_contr": "cod_contr",
            "base_imponible_t": "base_imponible_t",
            "base_imponible_t_1": "base_imponible_t_1",
            "fecha_data": "fecha_data",
        }
