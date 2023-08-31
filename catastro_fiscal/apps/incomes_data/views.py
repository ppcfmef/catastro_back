from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.lands.views import UploadHistoryViewset, UploadStatusViewSet
from .models import Contribuyente, MarcoPredio, Arancel, PredioDato
from .serializers import (
    IncomeUploadHistorySerializer, IncomeUploadStatusSerializer, RTContribuyenteSerializer, RTMarcoPredioSerializer,
    RTArancelSerializer, RTPredioDatoSerializer, RTPredioCaracteristicaSerializer, RTRecaudacionSerializer,
    RTDeudaSerializer, RTEmisionSerializer, RTBaseImponibleSerializer, RTAlicuotaSerializer,
    RTAmnistiaContribuyenteSerializer, RTAmnistiaMunicipalSerializer, RTVaremMunicipalSerializer
)


class IncomeUploadHistoryViewset(UploadHistoryViewset):
    create_serializer_class = IncomeUploadHistorySerializer


class IncomeUploadStatusViewSet(UploadStatusViewSet):
    serializer_class = IncomeUploadStatusSerializer


class RTContribuyenteViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Contribuyente.objects.all()
    serializer_class = RTContribuyenteSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTMarcoPredioViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = MarcoPredio.objects.all()
    serializer_class = RTMarcoPredioSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTArancelViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Arancel.objects.all()
    serializer_class = RTArancelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTPredioDatoViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTPredioDatoSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTPredioCaracteristicaViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTPredioCaracteristicaSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTRecaudacionViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTRecaudacionSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTDeudaViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTDeudaSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTEmisionViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTEmisionSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTBaseImponibleViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTBaseImponibleSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTAlicuotaViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTAlicuotaSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTAmnistiaContribuyenteViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTAmnistiaContribuyenteSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTAmnistiaMunicipalViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTAmnistiaMunicipalSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]


class RTVaremMunicipalViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PredioDato.objects.all()
    serializer_class = RTVaremMunicipalSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['ubigeo', ]
