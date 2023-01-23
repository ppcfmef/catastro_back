from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from apps.users.models import RolePermission, PermissionNavigation
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
        user = self.request.user
        if user.is_superuser:
            return self.get_recursive_admin(queryset=self.queryset)
        return self.get_recursive(role=user.role, queryset=self.queryset)

    def get_recursive_admin(self, queryset):
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

    def get_recursive(self, role, queryset):
        permissions = RolePermission.objects.filter(role=role).values_list('permission', flat=True)
        permission_navigation = PermissionNavigation.objects \
            .filter(permission__in=permissions, type__code__startswith='read')
        navigations = permission_navigation.values_list('navigation_view', flat=True)
        parents = list(
            queryset.filter(id__in=navigations).exclude(parent__isnull=True).values_list('parent', flat=True))
        parent_basic = list(queryset.filter(id__in=navigations, parent__isnull=True).values_list('id', flat=True))
        parents = parents + parent_basic
        parents.append('home')
        queryset_group = queryset.filter(id__in=parents).order_by('order')
        group_values = list(queryset_group.values())
        group_list = []
        for group in group_values:
            queryset_item = queryset.filter(parent_id=group['id'], id__in=navigations).values()
            group.update({'children': list(queryset_item)})
            group_list.append(group)
        return group_list


class NavigationManageViewset(ModelViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer


class NavigationViewViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = super(NavigationViewViewset, self).get_queryset()
        return queryset.filter(type='basic').exclude(id='home')
