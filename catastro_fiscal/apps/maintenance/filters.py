import django_filters
from .models import ApplicationResultDetail, Application,Result

class ApplicationFilter(django_filters.FilterSet):
    cup = django_filters.CharFilter(field_name='lands__land__cup', lookup_expr='icontains')
    ubigeo = django_filters.CharFilter(field_name='ubigeo', lookup_expr='exact')
    id_type = django_filters.CharFilter(field_name='id_type', lookup_expr='exact')
    id_status = django_filters.CharFilter(field_name='id_status', lookup_expr='exact')
    class Meta:
        model =  Application
        fields = ['cup','ubigeo','id_type','id_status']