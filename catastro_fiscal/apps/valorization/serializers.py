from rest_framework import serializers, exceptions
from .models import (
    Photo,PhotoType
)
import base64
from django.db import transaction
from django.conf import settings
from django.core.files import File
class PhotoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoType
        fields = '__all__'  # ToDo: estandarizar listado de predios


class PhotoSerializer(serializers.ModelSerializer):
    desc_tipo_foto =  serializers.CharField(source='cod_tipo_foto.desc_tipo_foto',read_only=True)
    class Meta:
        model = Photo
        fields = '__all__'  # ToDo: estandarizar listado de predios
    
    
    # def photo_base64_to_jpg(self, tb_photo, photo):
    #     tmp_upload = settings.MEDIA_ROOT / 'tmp_uploads'
    #     tmp_upload.mkdir(parents=True, exist_ok=True)

    #     cod_location = tb_photo.get('cod_ubicacion')
    #     cod_photo = tb_photo.get('cod_foto')
    #     photo_base64 = tb_photo.get('url_foto')
    #     file_name = f'{cod_location}_{cod_photo}.jpg'
    #     file_path = tmp_upload / file_name

    #     try:
    #         image = base64.b64decode(photo_base64)
    #         with open(file_path, "wb") as f:
    #             f.write(image)

    #         photo.url_foto.save(file_name, File(open(file_path, 'rb')))

    #     except Exception as e:
    #         print(f'error al cargar imagen imagen {cod_photo}')
    
    
    # @transaction.atomic
    # def save(self, **kwargs):
    #     tb_photo = dict(self.validated_data)
        
    #     photo = Photo.objects.create(
    #         cod_ubicacion=tb_photo.get('cod_ubicacion'),
    #         cod_foto=tb_photo.get('cod_foto'),
    #         cod_tipo_foto_id=self.blank_to_null(tb_photo.get('cod_tipo_foto', None)),
    #         url_foto=None
    #     )
        
    #     self.photo_base64_to_jpg(tb_photo, photo)


class PhotoSaveMobileSerializer(serializers.Serializer):
    
    cod_foto = serializers.CharField()
    cod_ubicacion = serializers.CharField()
    cod_tipo_foto = serializers.CharField()
    url_foto = serializers.CharField()

    def blank_to_null(self, value):
        if value == "":
            return None
        return value
    
    def photo_base64_to_jpg(self, tb_photo, photo):
        tmp_upload = settings.MEDIA_ROOT / 'tmp_uploads'
        tmp_upload.mkdir(parents=True, exist_ok=True)

        cod_location = tb_photo.get('cod_ubicacion')
        cod_photo = tb_photo.get('cod_foto')
        photo_base64 = tb_photo.get('url_foto')
        cod_tipo_foto = tb_photo.get('cod_tipo_foto', None)
        file_name = f'{cod_location}_{cod_tipo_foto}.jpg'
        file_path = tmp_upload / file_name

        try:
            image = base64.b64decode(photo_base64)
            with open(file_path, "wb") as f:
                f.write(image)

            photo.url_foto.save(file_name, File(open(file_path, 'rb')))

        except Exception as e:
            print(f'error al cargar imagen imagen {cod_photo}')
    
    
    @transaction.atomic
    def save(self, **kwargs):
        tb_photo = dict(self.validated_data)
        
        photo = Photo.objects.create(
            cod_ubicacion=tb_photo.get('cod_ubicacion'),
            cod_foto=tb_photo.get('cod_foto'),
            cod_tipo_foto_id=self.blank_to_null(tb_photo.get('cod_tipo_foto', None)),
            url_foto=None
        )
        
        self.photo_base64_to_jpg(tb_photo, photo)
        #photos = list(tb_location.get('tb_foto', []))
        
        #for photo in photos:
            #tb_photo = dict(photo)
            #self.create_photo(tb_photo, location)
    
