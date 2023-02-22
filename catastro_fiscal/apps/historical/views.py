from django.shortcuts import render
from rest_framework import mixins, status
from .models import HistoricalRecord
from .serializers import HistoricalSerializer, HistoricalUserSerializer
from rest_framework.viewsets import GenericViewSet
from django.db.models import Count


class HistoricalRecordViewset(mixins.ListModelMixin, GenericViewSet):

    queryset = HistoricalRecord.objects.none()
    serializer_class = HistoricalSerializer

    def get_queryset(self):
        department = self.request.GET.get("department")
        province = self.request.GET.get("province")
        district = self.request.GET.get("district")
        institution = self.request.GET.get("institution")

        if department and province and district and institution:
            self.queryset = HistoricalRecord.objects.values(
                'registered_by__id', 'registered_by__dni', 'registered_by__first_name', 'registered_by__last_name', 'registered_by__role__name'
                ).annotate(
                    actions_total=Count('registered_by')
                ).filter(
                    registered_by__department=department,
                    registered_by__province=province,
                    registered_by__district=district,
                    registered_by__institution=institution
                )
        return self.queryset


class HistoricalRecordByUserViewset(mixins.ListModelMixin, GenericViewSet):

    queryset = HistoricalRecord.objects.none()
    serializer_class = HistoricalUserSerializer

    def get_queryset(self):
        username = self.request.GET.get("username") or self.request.GET.get("search")
        return HistoricalRecord.objects.filter(registered_by__username=username).order_by('-creation_date')
