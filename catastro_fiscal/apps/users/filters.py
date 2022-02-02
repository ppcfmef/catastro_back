import django_filters
from .models import User


class UserCustomFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date_joined', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date_joined', lookup_expr='lt')

    class Meta:
        model = User
        fields = ('is_active', 'role', 'start_date', 'end_date')
