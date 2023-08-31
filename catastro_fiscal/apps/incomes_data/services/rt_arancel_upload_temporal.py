from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import Arancel


class ArancelValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arancel
        fields = '__all__'


class RTArancelUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = ArancelValidSerializer

    def mapper(self):
        return {
            "ano_ejec": "ano_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "id_cl": "id_cl",
            "sector_catastral": "sector_catastral",
            "manzana_catastral": "manzana_catastral",
            "codigo_via": "codigo_via",
            "denominacion_de_via": "denominacion_de_via",
            "lado_imp_par": "lado_imp_par",
            "cuadra_de_via": "cuadra_de_via",
            "cod_hab_urbana": "cod_hab_urbana",
            "habilit_urbana": "habilit_urbana",
            "mza_urbana": "mza_urbana",
            "ubica_parque_jardin_id": "ubica_parque_jardin_id",
            "ano_arancelario": "ano_arancelario",
            "arancel": "arancel",
            "ano_x_procesar": "ano_x_procesar",
            "arancel_actual": "arancel_actual",
            "fila": "fila",
            "id_arancel": "id_arancel",
            "fecha_data": "fecha_data",
        }
