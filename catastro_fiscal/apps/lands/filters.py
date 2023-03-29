import django_filters
from .models import LandOwner


class LandOwnerFilter(django_filters.FilterSet):
    ubigeo = django_filters.CharFilter(field_name="land__ubigeo")

    class Meta:
        model = LandOwner
        fields = ['dni', 'name', 'paternal_surname', 'maternal_surname', 'ubigeo', ]
