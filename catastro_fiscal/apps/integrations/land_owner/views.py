from rest_framework.response import Response
from rest_framework.views import APIView
from .nsrtm.services import NsrtmLandOwnerService
from .sat.services import SattLandOwnerService
from .serializers import IntegrationResponseSerializer


class GetLandOwnerView(APIView):
    ubigeo_tarapoto = '220901'

    def get(self, request, *args, **kwargs):
        ubigeo = kwargs.get('ubigeo')
        land_owner = kwargs.get('land_owner')
        data = self.get_provider_data(ubigeo, land_owner)
        serializer = IntegrationResponseSerializer(data)
        return Response(serializer.data)

    def get_provider_data(self, ubigeo, land_owner):
        if ubigeo == self.ubigeo_tarapoto:
            return SattLandOwnerService().get(land_owner=land_owner)
        return NsrtmLandOwnerService().get(ubigeo=ubigeo, land_owner=land_owner)
