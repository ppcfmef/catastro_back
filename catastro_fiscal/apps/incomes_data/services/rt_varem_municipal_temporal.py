from rest_framework import serializers
from .income_upload_temporal import IncomeUploadTemporalService
from ..models import VaremMunicipal


class VaremMunicipalValidSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaremMunicipal
        fields = '__all__'


class RTVaremMunicipalUploadTemporalService(IncomeUploadTemporalService):
    valid_serializer = VaremMunicipalValidSerializer

    def mapper(self):
        return {
            "anio_ejec": "anio_ejec",
            "ubigeo": "ubigeo",
            "sec_ejec": "sec_ejec",
            "muni_2802": "muni_2802",
            "muni_3103": "muni_3103",
            "muni_xx": "muni_xx",
            "nro_contrib_t": "nro_contrib_t",
            "nro_contrib_t_1": "nro_contrib_t_1",
            "nro_ord_x_amnistia": "nro_ord_x_amnistia",
            "nro_pred_inafecto": "nro_pred_inafecto",
            "base_imponible_exento": "base_imponible_exento",
            "nro_pred_am": "nro_pred_am",
            "monto_ip_am": "monto_ip_am",
            "fecha_data": "fecha_data",
        }
