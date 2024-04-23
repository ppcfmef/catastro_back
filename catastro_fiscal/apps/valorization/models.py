from django.db import models
from django.utils.translation import gettext_lazy as _

class PhotoType(models.Model):
    cod_tipo_foto = models.CharField(primary_key=True,max_length=5)
    desc_tipo_foto = models.CharField(max_length=100, null=True,blank=True)
    class Meta:
        db_table = 'OFERTAS_INMOBILIARIAS_TIPO_FOTO'
        verbose_name = _('Offer Photo Type')
        verbose_name_plural = _('Offer Photo Type')

    def __str__(self):
        return self.desc_tipo_foto
    


class Photo(models.Model):
    cod_foto = models.CharField(primary_key=True,max_length=100)
    cod_ubicacion = models.CharField(max_length=100, null=True,blank=True)
    cod_tipo_foto = models.ForeignKey(PhotoType, on_delete=models.DO_NOTHING , null=True,blank=True)
    url = models.ImageField(upload_to='valorization', blank=True, null=True)  # ToDo: genera url
    class Meta:
        db_table = 'OFERTAS_INMOBILIARIAS_FOTO'
        verbose_name = _('Photo ')
        verbose_name_plural = _('Photo ')

    def __str__(self):
        return self.cod_foto