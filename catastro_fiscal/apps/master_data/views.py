from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .serializers import InstitutionSerializer, MasterDomainSerilizer
from .models import (
    Institution, MasterTypeUrbanUnit, MasterSide, MasterCodeStreet, MasterPropertyType, MasterResolutionType
)


class InstitutionViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    pagination_class = None


class MasterDomainView(APIView):
    serializer_class = MasterDomainSerilizer

    def get(self, request, *args, **kwargs):
        data = {
            "uu_type": MasterTypeUrbanUnit.objects.all(),
            "cod_street": MasterCodeStreet.objects.all(),
            "property_type": MasterPropertyType.objects.all(),
            "cod_side": MasterSide.objects.all(),
            'resolution_type': MasterResolutionType.objects.all(),
        }
        serializer = MasterDomainSerilizer(data)
        return Response(serializer.data)

    @classmethod
    def get_extra_actions(cls):
        return []
