from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .serializers import InstitutionSerializer, MasterDomainSerilizer,MasterResolutionTypeSerializer
from .models import (
    Institution, MasterTypeUrbanUnit, MasterSide, MasterCodeStreet, MasterTipoPredio, MasterResolutionType, ResolutionTypeDistrito
)

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import CamelCaseOrderFilter
from rest_framework.decorators import authentication_classes ,permission_classes
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
            "property_type": MasterTipoPredio.objects.all(),
            "cod_side": MasterSide.objects.all(),
            'resolution_type': MasterResolutionType.objects.all(),
        }
        serializer = MasterDomainSerilizer(data)
        return Response(serializer.data)

    @classmethod
    def get_extra_actions(cls):
        return []

@authentication_classes([])
@permission_classes([])
class  MasterResolutionView(mixins.ListModelMixin, GenericViewSet):
    queryset = MasterResolutionType.objects.all()
    serializer_class = MasterResolutionTypeSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend,  CamelCaseOrderFilter]
    filterset_fields = ['estado_registro','estado_mantenimiento']

    def list(self, request, *args, **kwargs):
        ubigeo=request.query_params.get('ubigeo')
        data=self.filter_queryset(self.queryset.filter(tipo=1,estado =1))
        serializer=MasterResolutionTypeSerializer(data, many = True)
        resolucion_por_distrito=ResolutionTypeDistrito.objects.filter(ubigeo_id = ubigeo,estado =1)
        data2=self.queryset.filter(id__in =resolucion_por_distrito.values_list('resolucion_id',flat=True))
        serializer2 = MasterResolutionTypeSerializer(data2, many = True)
        return Response(serializer.data + serializer2.data)


 