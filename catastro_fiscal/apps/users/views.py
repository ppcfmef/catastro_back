from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from drf_yasg.utils import swagger_auto_schema
from core.views import CustomListMixin
from .serializers import (
    UserProfileShortSerializer, UserSerializer, UserListSerializer, UserDetailSerializer, RoleSerializer,
    RoleShortSerializer, PermissionSerializer, PermissionListSerializer, PermissionTypeSerializer,
    PermissionNavigationSerializer, RoleListSerializer
)
from .models import User, Role, Permission, PermissionType, PermissionNavigation
from .filters import UserCustomFilter


class UserProfileShortView(APIView):
    queryset = User.objects.all()
    serializer_class = UserProfileShortSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, context={"request": request})
        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer
    filter_class = UserCustomFilter
    filterset_fields = ['is_active', 'role', 'start_date', 'end_date']

    @swagger_auto_schema(responses={200: UserListSerializer()})
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().exclude(is_superuser=True))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: UserListSerializer()})
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.detail_serializer_class(instance, context={"request": request})
        return Response(serializer.data)


class RoleViewSet(CustomListMixin, ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    list_serializer_class = RoleListSerializer

    @swagger_auto_schema(responses={200: RoleListSerializer()})
    def list(self, request, *args, **kwargs):
        return super(RoleViewSet, self).custom_list(request, *args, **kwargs)


class RoleSelectViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleShortSerializer
    pagination_class = None


class PermissionViewSet(CustomListMixin, ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    list_serializer_class = PermissionListSerializer

    @swagger_auto_schema(responses={200: PermissionListSerializer()})
    def list(self, request, *args, **kwargs):
        return super(PermissionViewSet, self).custom_list(request, *args, **kwargs)


class PermissionSelectViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionListSerializer
    pagination_class = None


class PermissionTypeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PermissionType.objects.all()
    serializer_class = PermissionTypeSerializer
    pagination_class = None


class PermissionNavigationViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = PermissionNavigation.objects.all()
    serializer_class = PermissionNavigationSerializer
    pagination_class = None

    def get_queryset(self):
        id_permission = self.kwargs.get('id_permission')
        queryset = super(PermissionNavigationViewSet, self).get_queryset()
        return queryset.filter(permission_id=id_permission)
