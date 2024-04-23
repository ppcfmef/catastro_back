from rest_framework.decorators import authentication_classes ,permission_classes
from rest_framework.viewsets import GenericViewSet ,ModelViewSet
from .serializers import PhotoSerializer
from .models import Photo
from rest_framework.filters import SearchFilter
from core.filters import CamelCaseOrderFilter
from django_filters.rest_framework import DjangoFilterBackend

@authentication_classes([])
@permission_classes([])
class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    
    