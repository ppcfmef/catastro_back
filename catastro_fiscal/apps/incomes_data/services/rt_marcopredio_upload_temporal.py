from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import MarcoPredio


class MarcoPredioValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcoPredio
        fields = '__all__'


class RTMarcoPredioUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = MarcoPredioValidSerializer

    def mapper(self):
        return {
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "cod_pre": "cod_pre",
            "codigo_cpu": "codigo_cpu",
            "nombre_predio": "nombre_predio",
            "habilitacion": "habilitacion",
            "nombre_habilitacion": "nombre_habilitacion",
            "nombre_tipo_habilitacion": "nombre_tipo_habilitacion",
            "via": "via",
            "nombre_tipo_via": "nombre_tipo_via",
            "nombre_via": "nombre_via",
            "manzana_urbana": "manzana_urbana",
            "cuadra": "cuadra",
            "lado": "lado",
            "numero_direccion": "numero_direccion",
            "numero_alterno": "numero_alterno",
            "block": "block",
            "numero_departamento": "numero_departamento",
            "interior": "interior",
            "lote": "lote",
            "km": "km",
            "estado": "estado",
            "es_independizado": "es_independizado",
            "tipo_titulacion": "tipo_titulacion",
            "desc_titulo": "desc_titulo",
            "codigo_predio_titulo": "codigo_predio_titulo",
            "numero_unidad_catastral": "numero_unidad_catastral",
            "codigo_referencia_catastral": "codigo_referencia_catastral",
            "numero_parcela_agricola": "numero_parcela_agricola",
            "numero_partida_registral": "numero_partida_registral",
            "perimetro": "perimetro",
            "referencia": "referencia",
            "id_cl": "id_cl",
            "fecha_data": "fecha_data",
        }
