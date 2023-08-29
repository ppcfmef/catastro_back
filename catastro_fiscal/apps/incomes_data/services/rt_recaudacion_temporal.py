from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import Recaudacion


class RecaudacionValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recaudacion
        fields = '__all__'


class RTRecaudacionUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = RecaudacionValidSerializer

    def mapper(self):
        return {
            "ano_ejec": "ano_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "cod_contr": "cod_contr",
            "rec_imp_pred": "rec_imp_pred",
            "rec_arb": "rec_arb",
            "rec_imp_veh": "rec_imp_veh",
            "rec_imp_pred_nc": "rec_imp_pred_nc",
            "rec_arb_nc": "rec_arb_nc",
            "rec_imp_veh_nc": "rec_imp_veh_nc",
            "rec_op_p_c": "rec_op_p_c",
            "rec_op_p_nc": "rec_op_p_nc",
            "rec_rd_p_c": "rec_rd_p_c",
            "rec_rd_p_nc": "rec_rd_p_nc",
            "rec_res_determ_arb": "rec_res_determ_arb",
            "rec_res_ejec_coactiva_predial": "rec_res_ejec_coactiva_predial",
            "rec_res_ejec_coactiva_arbitrios": "rec_res_ejec_coactiva_arbitrios",
            "fecha_data": "fecha_data",
        }
