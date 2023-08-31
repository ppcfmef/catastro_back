from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import AmnistiaContribuyente


class AmnistiaContribuyenteValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmnistiaContribuyente
        fields = '__all__'


class RTAmnistiaContribuyenteUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = AmnistiaContribuyenteValidSerializer

    def mapper(self):
        return {
            "anio_ejec": "anio_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "cod_tipo_amn": "cod_tipo_amn",
            "cod_contr": "cod_contr",
            "tributo_afecto": "tributo_afecto",
            "tipo_periodo": "tipo_periodo",
            "periodo": "periodo",
            "tipo_int_ins": "tipo_int_ins",
            "porc_desc": "porc_desc",
            "fecha_data": "fecha_data",
        }
