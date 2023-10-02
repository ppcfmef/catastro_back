from django.db.models import Q, Count, OuterRef, Subquery
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from apps.lands.models import Land
from core.views import CustomListMixin
from .serializers import (
    UserProfileShortSerializer, UserSerializer, UserListSerializer, UserDetailSerializer, RoleSerializer,
    RoleShortSerializer, PermissionSerializer, PermissionListSerializer, PermissionTypeSerializer,
    PermissionNavigationSerializer, RoleListSerializer, InstitutionListSerializer
)
from .models import User, Role, Permission, PermissionType, PermissionNavigation
from .filters import UserCustomFilter
from apps.historical.models import HistoricalRecord
import requests
from django.conf import settings

class UserProfileShortView(APIView):
    queryset = User.objects.all()
    serializer_class = UserProfileShortSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, context={"request": request})
        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = UserCustomFilter
    filterset_fields = ['is_active', 'role', 'start_date', 'end_date', 'institution', 'department', 'province', 'district']
    search_fields = ['dni', 'district__code', 'district__name']

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save()
        HistoricalRecord.register(user, serializer.instance, type_event=HistoricalRecord.RecordEvent.UPDATED)

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

    @action(detail=False, methods=['get'])
    def institutions(self, request, *args, **kwargs):
        user = request.user
        queryset = User.objects.select_related('institution').values(
            'institution', 'place_scope', 'department', 'province', 'district', 'department__name', 'province__name', 'district__name'
        ).filter(~Q(institution=None))
        if user.place_scope_id > 1 and not user.is_superuser:
            if user.place_scope_id == 2:
                queryset = queryset.filter(
                    Q(department=user.department),
                    Q(place_scope_id__gte=user.place_scope_id))
            elif user.place_scope_id == 3:
                queryset = queryset.filter(
                    Q(department=user.department),
                    Q(province=user.province),
                    Q(place_scope_id__gte=user.place_scope_id))
            elif user.place_scope_id == 4:
                queryset = queryset.filter(
                    Q(department=user.department),
                    Q(province=user.province),
                    Q(district=user.district),
                    Q(place_scope_id__gte=user.place_scope_id))
        if request.GET.get("search"):
            search = request.GET.get("search")
            queryset = queryset.filter(Q(institution__name__icontains=search))
        queryset = queryset.distinct()
        serializer = InstitutionListSerializer(queryset, many=True)
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


def jwt_response_payload_handler(token, user=None, request=None):

    # params = {
    #         'username': 'admin.portal',
    #                     'password': 'ags.2022',
    #                     'f': 'json',  # Formato de respuesta JSON
    #                     'client':'referer',
    #                     'referer':'http://localhost:4200/',
    #                     'expiration':5000,
    #                 }

                    # Realiza la solicitud POST para obtener el token
    #response = requests.post(settings.AUTH_URL_ARCGIS, data=params)

                    # Verifica si la solicitud fue exitosa
    #if response.status_code == 200:
                        # El token se encuentra en la respuesta JSON
        #tokenArcGis = response.json()['token']
        
        
    #else:
                       

    tokenArcGis=''
    return {
        'token': token,
        'tokenArcGis': tokenArcGis
    }