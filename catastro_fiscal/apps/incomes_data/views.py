from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.lands.views import UploadHistoryViewset, UploadStatusViewSet
from .models import Contribuyente, MarcoPredio, Arancel, PredioDato
from .serializers import (
    IncomeUploadHistorySerializer, IncomeUploadStatusSerializer, RTContribuyenteSerializer, RTMarcoPredioSerializer,
    RTArancelSerializer, RTPredioDatoSerializer
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
