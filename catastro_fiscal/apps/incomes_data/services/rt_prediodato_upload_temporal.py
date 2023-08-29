from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import PredioDato


class PredioDatoValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredioDato
        fields = '__all__'


class RTPredioDatoUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = PredioDatoValidSerializer

    def mapper(self):
        return {
            "sec_ejec": "sec_ejec",
            "ubigeo": "ubigeo",
            "ano_aplicacion": "ano_aplicacion",
            "cod_contr": "cod_contr",
            "cod_pre": "cod_pre",
            "cond_predio": "cond_predio",
            "fecha_recepcion": "fecha_recepcion",
            "codigo_uso": "codigo_uso",
            "uso_especifico": "uso_especifico",
            "tipo_predio": "tipo_predio",
            "estado_const": "estado_const",
            "condicion_prop": "condicion_prop",
            "porcentaje_copropiedad": "porcentaje_copropiedad",
            "area_terreno": "area_terreno",
            "area_terreno_comun": "area_terreno_comun",
            "arancel": "arancel",
            "valor_terreno_urbano": "valor_terreno_urbano",
            "area_construida": "area_construida",
            "valor_total_construccion": "valor_total_construccion",
            "valor_otras_instalaciones": "valor_otras_instalaciones",
            "valor_predio": "valor_predio",
            "imp_predial": "imp_predial",
            "fecha_data": "fecha_data",
        }
