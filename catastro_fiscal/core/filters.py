from rest_framework.filters import OrderingFilter
from core.utils.parser import CamelCaseToSnake


class CamelCaseOrderFilter(OrderingFilter):
    def get_ordering(self, request, queryset, view):
        params = request.query_params.get(self.ordering_param)
        if params:
            fields = [CamelCaseToSnake.exec(param.strip()) for param in params.split(',')]
            ordering = self.remove_invalid_fields(queryset, fields, view, request)
            if ordering:
                return ordering
        return self.get_default_ordering(view)
