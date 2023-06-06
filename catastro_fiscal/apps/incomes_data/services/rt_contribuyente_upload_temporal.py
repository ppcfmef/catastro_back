from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import Contribuyente


class ContribuyenteValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuyente
        fields = '__all__'


class RTContribuyenteUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = ContribuyenteValidSerializer

    def mapper(self):
        return {
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "cod_contr": "cod_contr",
            "fecha_inscripcion": "fecha_inscripcion",
            "tipo_doc": "tipo_doc",
            "documento_desc": "documento_desc",
            "num_doc": "num_doc",
            "apellido_paterno": "apellido_paterno",
            "apellido_materno": "apellido_materno",
            "nombre": "nombre",
            "tipo_contribuyente_desc": "tipo_contribuyente_desc",
            "condicion_contribuyente_desc": "condicion_contribuyente_desc",
            "estado": "estado",
            "es_foraneo": "es_foraneo",
            "distrito_desc": "distrito_desc",
            "provincia_desc": "provincia_desc",
            "departamento_desc": "departamento_desc",
            "tipo_habilitacion_desc": "tipo_habilitacion_desc",
            "nombre_habilitacion": "nombre_habilitacion",
            "tipo_via_desc": "tipo_via_desc",
            "nombre_via": "nombre_via",
            "manzana_urbana": "manzana_urbana",
            "cuadra": "cuadra",
            "lado": "lado",
            "numero_direccion": "numero_direccion",
            "numero_alterno": "numero_alterno",
            "numero_departamento": "numero_departamento",
            "lote": "lote",
            "interior": "interior",
            "block": "block",
            "es_pensionista": "es_pensionista",
            "fecha_data": "fecha_data",
        }
