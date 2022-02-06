from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from .serializers import NavigationTreeSerializer, NavigationSerializer
from .models import Navigation


class NavigationViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationTreeSerializer
    pagination_class = None

    @swagger_auto_schema(responses={200: NavigationTreeSerializer()})
    def list(self, request, *args, **kwargs):
        return super(NavigationViewset, self).list(mixins.ListModelMixin, GenericViewSet)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.get_recursive(queryset=self.queryset)
        return self.get_recursive(queryset=self.queryset)

    def get_recursive(self, queryset):
        queryset_group = queryset.filter(parent__isnull=True)
        group_values = list(queryset_group.values())
        group_list = []
        for group in group_values:
            queryset_module = queryset.filter(parent_id=group['id'])
            module_values = list(queryset_module.values())
            module_list = []
            for module in module_values:
                queryset_item = queryset.filter(parent_id=module['id']).values()
                module.update({'children': list(queryset_item)})
                module_list.append(module)
            group.update({'children': module_list})
            group_list.append(group)
        return group_list


class NavigationManageViewset(ModelViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer
