from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserProfileShortSerializer, UserSerializer, UserListSerializer, UserDetailSerializer
from .models import User
from .filters import UserCustomFilter


class UserProfileShortView(APIView):
    queryset = User.objects.all()
    serializer_class = UserProfileShortSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
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
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: UserListSerializer()})
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.detail_serializer_class(instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = super(UserViewSet, self).get_queryset().exclude(is_superuser=True)
        return queryset
