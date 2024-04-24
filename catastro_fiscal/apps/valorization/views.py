from rest_framework.decorators import authentication_classes ,permission_classes
from rest_framework.viewsets import GenericViewSet ,ModelViewSet
from .serializers import PhotoSerializer,PhotoSaveMobileSerializer
from .models import Photo
from rest_framework.filters import SearchFilter
from core.filters import CamelCaseOrderFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, exceptions

@authentication_classes([])
@permission_classes([])
class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, CamelCaseOrderFilter]
    filterset_fields = ['cod_ubicacion','cod_foto' ]
    
    @action(methods=['post'], detail=False, url_path='guardar-fotos')
    def guardar_fotos(self, request, *args, **kwargs):
        #cod_ubicacion = request.data.get(cod_ubicacion)
        
        #photos=request.data.get('photos',None)
        
        try:
            
            #for data in photos:
                #serializer=PhotoSaveMobileSerializer(data=data)
                #serializer.is_valid(raise_exception=True)
                #serializer.save()
            serializer=PhotoSaveMobileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_serializer = {
                "status": "success",
                "message": "Los registros se guardaron correctamente"
            }
        except Exception as e:
            response_serializer = {
                "status": "error",
                "message": str(e)
            }
            raise exceptions.ValidationError(response_serializer)
        
        return Response(response_serializer, status=status.HTTP_201_CREATED)
        
        # try:
        #     for data in photos:
        #         serializer=PhotoSerializer(data=data)
        #         serializer.is_valid(raise_exception=True)
        #         serializer.save()
            
        #     return Res
        
        
        