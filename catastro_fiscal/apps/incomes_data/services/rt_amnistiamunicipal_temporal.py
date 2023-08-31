from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import AmnistiaMunicipal


class AmnistiaMunicipalValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmnistiaMunicipal
        fields = '__all__'


class RTAmnistiaMunicipalUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = AmnistiaMunicipalValidSerializer

    def mapper(self):
        return {
            "anio_ejec": "anio_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "tipo_amn_benef": "tipo_amn_benef",
            "nomb_amn_benef": "nomb_amn_benef",
            "nro_ordenanza": "nro_ordenanza",
            "fecha_ini": "fecha_ini",
            "fecha_fin": "fecha_fin",
            "tributo_afecto": "tributo_afecto",
            "tipo_periodo": "tipo_periodo",
            "periodo": "periodo",
            "tipo_int_ins": "tipo_int_ins",
            "porc_desc": "porc_desc",
            "fecha_data": "fecha_data",
        }
