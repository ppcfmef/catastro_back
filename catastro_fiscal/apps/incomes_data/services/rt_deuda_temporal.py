from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import Deuda


class DeudaValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deuda
        fields = '__all__'


class RTDeudaUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = DeudaValidSerializer

    def mapper(self):
        return {
            "ano_ejec": "ano_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "cod_contr": "cod_contr",
            "deuda_arb": "deuda_arb",
            "saldo_t_p": "saldo_t_p",
            "saldo_t_1_p": "saldo_t_1_p",
            "saldo_t_v": "saldo_t_v",
            "saldo_t_a": "saldo_t_a",
            "saldo_t_1_a": "saldo_t_1_a",
            "ano_deuda_t": "ano_deuda_t",
            "ano_deuda_p": "ano_deuda_p",
            "ano_deuda_v": "ano_deuda_v",
            "fecha_data": "fecha_data",
        }
