from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
from rest_framework.response import Response
from .serializers import HistoricalSerializer, HistoricalUserSerializer, HistoricalRecordSerializer, HistoricalRecord
from rest_framework.viewsets import GenericViewSet
from django.db.models import Count


class HistoricalRecordViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):

    queryset = HistoricalRecord.objects.none()
    serializer_class = HistoricalSerializer

    def get_queryset(self):
        department = self.request.GET.get("department")
        province = self.request.GET.get("province")
        district = self.request.GET.get("district")
        institution = self.request.GET.get("institution")

        self.queryset = HistoricalRecord.objects.values(
            'registered_by__id', 'registered_by__dni', 'registered_by__first_name', 'registered_by__last_name', 'registered_by__role__name'
            ).annotate(
                actions_total=Count('registered_by')
            ).filter(
                registered_by__institution=institution
            )

        if str(department).isnumeric():
            self.queryset = self.queryset.filter(registered_by__department=department)
        if str(province).isnumeric():
            self.queryset = self.queryset.filter(registered_by__province=province)
        if str(district).isnumeric():
            self.queryset = self.queryset.filter(registered_by__district=district)

        return self.queryset

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(HistoricalRecord, pk=kwargs.get("pk"))
        serializer = HistoricalRecordSerializer(instance, context={"request": request})
        return Response(serializer.data)


class HistoricalRecordByUserViewset(mixins.ListModelMixin, GenericViewSet):

    queryset = HistoricalRecord.objects.none()
    serializer_class = HistoricalUserSerializer

    def get_queryset(self):
        username = self.request.GET.get("username") or self.request.GET.get("search")
        return HistoricalRecord.objects.filter(registered_by__username=username).order_by('-creation_date')
