import django_filters
from .models import LandOwner


class LandOwnerFilter(django_filters.FilterSet):
    ubigeo = django_filters.CharFilter(field_name="lands__ubigeo",distinct=True)

    class Meta:
        model = LandOwner
        fields = ['id', 'dni', 'ubigeo', ]
