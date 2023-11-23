import requests
from .serializers import SattValidateSerializer
from ..services import LandOwnerIntegrateService


class SattLandOwnerService(LandOwnerIntegrateService):
    url_api_env = 'URL_API_SATT'
    default_ubigeo = "220901"

    def get(self, **kwargs):
        ubigeo = self.default_ubigeo
        land_owner = kwargs.get('land_owner')
        return self.get_data(ubigeo, land_owner)

    def get_data(self, ubigeo, land_owner):
        url_api = self.get_url_api()
        r = requests.get(f'{url_api}/{ubigeo}/{land_owner}')
        if r.status_code != 200:
            raise self.exception()
        return self.map_data(data=r.json())

    def map_data(self, data):
        serializer_valid = SattValidateSerializer(data=data)
        serializer_valid.is_valid(raise_exception=False)
        valid_data = serializer_valid.data
        status = valid_data.get('status', None)
        data_items = valid_data.get('data', [])

        if len(list(data_items)) == 0 or status != 200:
            raise self.exception()

        data = data_items[0]

        return {
            "document_type": '01',
            "document": data.get('nrodocumento'),
            "nane": self.clean_str(data=data.get('nombre')),
            "paternal_surname": self.clean_str(data=data.get('appaterno')),
            "maternal_surname": self.clean_str(data=data.get('apmaterno')),
        }
