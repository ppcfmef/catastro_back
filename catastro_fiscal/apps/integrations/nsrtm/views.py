import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NsrtmLandOwnerSerializer


class GetNsrtmLandOwnerView(APIView):

    def get(self, request, *args, **kwargs):
        ubigeo = kwargs.get('ubigeo')
        land_owner = kwargs.get('land_owner')
        data = self.get_data(ubigeo, land_owner)
        serializer = NsrtmLandOwnerSerializer(data)
        return Response(serializer.data)

    def get_url_api(self):
        return getattr(settings, 'URL_API_NSRTM')

    def get_key_api(self):
        return ""

    def get_data(self, ubigeo, land_owner):
        url_api = self.get_url_api()
        r = requests.get(f'{url_api}?ubigeo={ubigeo}&codigo_contribuyente={land_owner}')
        if r.status_code != 200:
            pass
        return self.map_data(r.json())

    def map_data(self, data):
        return {
            "document_type": int(data.get('tipoDocumento')),
            "document_type_description": data.get('tipoDocumentoDescripcion'),
            "document": data.get('numeroDocumento'),
            "nane": str(data.get('nombres')).capitalize(),
            "paternal_surname": str(data.get('paterno')).capitalize(),
            "maternal_surname": str(data.get('materno')).capitalize(),
            "business_name": str(data.get('razonSocial')).capitalize(),
        }
