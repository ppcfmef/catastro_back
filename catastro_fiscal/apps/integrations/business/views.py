import requests
from rest_framework.response import Response
from django.conf import settings
from rest_framework.views import APIView
from .serializers import BusinessIntegrationSerializer


class GetBusinessView(APIView):
    def get(self, request, *args, **kwargs):
        document = kwargs.get('document')
        data = self.get_data(document)
        serializer = BusinessIntegrationSerializer(data)
        return Response(serializer.data)

    def get_url_api(self):
        return getattr(settings, 'URL_API_BUSINESS')

    def get_key_api(self):
        return getattr(settings, 'KEY_API_BUSINESS')

    def get_data(self, document):
        url_api = self.get_url_api()
        key_api = self.get_key_api()
        r = requests.get(f'{url_api}/{document}/{key_api}/')
        if r.status_code != 200:
            pass
        return self.map_data(r.json())

    def map_data(self, data):
        return {
            "document": data.get('ruc'),
            "business_name": str(data.get('razon_social')).capitalize(),
        }
