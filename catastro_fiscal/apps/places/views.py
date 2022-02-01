from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import DepartmentSerializer, ProvinceSerializer, DistrictSerializer
from .models import Department, Province, District


class DepartmentSelectViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = None


class ProvinceSelectViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    pagination_class = None
    filterset_fields = ['department']


class DistrictSelectViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = None
    filterset_fields = ['province']
