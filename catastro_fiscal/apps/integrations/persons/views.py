import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonIntegrationSerializer


class GetPersonView(APIView):

    def get(self, request, *args, **kwargs):
        document = kwargs.get('document')
        data = self.get_data(document)
        serializer = PersonIntegrationSerializer(data)
        return Response(serializer.data)

    def get_url_api(self):
        return getattr(settings, 'URL_API_PERSONS')

    def get_key_api(self):
        return getattr(settings, 'KEY_API_PERSONS')

    def get_data(self, document):
        url_api = self.get_url_api()
        key_api = self.get_key_api()
        r = requests.get(f'{url_api}/{document}/{key_api}/')
        if r.status_code != 200:
            pass
        return self.map_data(r.json())

    def map_data(self, data):
        return {
            "document": data.get('dni'),
            "nane": str(data.get('nombres')).capitalize(),
            "paternal_surname": str(data.get('ap_paterno')).capitalize(),
            "maternal_surname": str(data.get('ap_materno')).capitalize(),
        }
