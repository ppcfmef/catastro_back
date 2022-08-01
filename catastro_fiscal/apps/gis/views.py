from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import GisCategory, GisCatalog, GisService
from .serializers import (
    GisCategorySerializer, GisCatalogListSerializer, GisCatalogDetailSerializer, GisServiceSerializer,
    GisCatalogCreateSerializer,
)


class GisCategoryViewSet(ModelViewSet):
    queryset = GisCategory.objects.all()
    serializer_class = GisCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['parent']
    ordering_fields = ['id', 'name', 'parent']


class GisCatalogViewSet(ModelViewSet):
    queryset = GisCatalog.objects.all()
    serializer_class = GisCatalogListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['category']
    ordering_fields = ['id', 'title', 'description', 'category']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GisCatalogDetailSerializer
        if self.action in ('create', 'update', 'partial_update'):
            return GisCatalogCreateSerializer
        return self.serializer_class


class GisServiceViewSet(ModelViewSet):
    queryset = GisService.objects.all()
    serializer_class = GisServiceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['catalog']
    ordering_fields = ['id', 'name']
