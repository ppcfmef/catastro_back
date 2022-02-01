from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import InstitutionSerializer
from .models import Institution


class InstitutionViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    pagination_class = None
