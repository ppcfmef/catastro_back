import requests
from .serializers import NsrtmLandOwnerSerializer
from ..services import LandOwnerIntegrateService


class NsrtmLandOwnerService(LandOwnerIntegrateService):
    url_api_env = 'URL_API_NSRTM'

    def get(self, **kwargs):
        ubigeo = kwargs.get('ubigeo')
        land_owner = kwargs.get('land_owner')
        data = self.get_data(ubigeo, land_owner)
        serializer = NsrtmLandOwnerSerializer(data)
        return serializer.data

    def get_data(self, ubigeo, land_owner):
        url_api = self.get_url_api()
        r = requests.get(f'{url_api}?ubigeo={ubigeo}&codigo_contribuyente={land_owner}')
        if r.status_code != 200:
            raise self.exception()
        return self.map_data(r.json())

    def map_data(self, data):
        return {
            "document_type": self.get_document_type(document_type=data.get('tipoDocumento')),
            "document": data.get('numeroDocumento'),
            "nane": self.clean_str(data=data.get('nombres')),
            "paternal_surname": self.clean_str(data=data.get('paterno')),
            "maternal_surname": self.clean_str(data=data.get('materno')),
            "business_name": self.clean_str(data=data.get('razonSocial')),
        }

    def get_document_type(self, document_type):
        document_type_map = {
            "1": "01",
            "2": "06"
        }

        if document_type in document_type_map:
            return document_type_map[document_type]

        return "01"
