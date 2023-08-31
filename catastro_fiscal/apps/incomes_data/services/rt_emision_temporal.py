from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import Emision


class EmisionValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emision
        fields = '__all__'


class RTEmisionUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = EmisionValidSerializer

    def mapper(self):
        return {
            "ano_ejec": "ano_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "cod_contr": "cod_contr",
            "emision_ord_pago": "emision_ord_pago",
            "emision_res_det": "emision_res_det",
            "emision_iv_corriente": "emision_iv_corriente",
            "emi_res_det_c": "emi_res_det_c",
            "emi_res_det_nc": "emi_res_det_nc",
            "emi_res_cp": "emi_res_cp",
            "emi_res_ca": "emi_res_ca",
            "fecha_data": "fecha_data",
        }
