from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import PredioCaracteristica


class PredioCaracteristicaValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredioCaracteristica
        fields = '__all__'


class RTPredioCaracteristicaUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = PredioCaracteristicaValidSerializer

    def mapper(self):
        return {
            "sec_ejec": "sec_ejec",
            "ubigeo": "ubigeo",
            "ano_aplicacion": "ano_aplicacion",
            "cod_contr": "cod_contr",
            "cod_pre": "cod_pre",
            "tipo_piso": "tipo_piso",
            "nivel": "nivel",
            "ano_construccion": "ano_construccion",
            "clasificacion_pred": "clasificacion_pred",
            "material_pred": "material_pred",
            "estado_conserva": "estado_conserva",
            "categoria_muro_columna": "categoria_muro_columna",
            "categoria_techo": "categoria_techo",
            "categoria_piso": "categoria_piso",
            "categoria_puerta_ventana": "categoria_puerta_ventana",
            "categoria_revestimiento": "categoria_revestimiento",
            "categoria_bano": "categoria_bano",
            "categoria_electrica": "categoria_electrica",
            "area_construida": "area_construida",
            "valor_unitario": "valor_unitario",
            "incremento": "incremento",
            "porcentaje_depreciacion": "porcentaje_depreciacion",
            "valor_unitario_depreciado": "valor_unitario_depreciado",
            "valor_nivel": "valor_nivel",
            "porcentaje_comun": "porcentaje_comun",
            "total_area_bien_comun": "total_area_bien_comun",
            "fecha_data": "fecha_data",
        }
