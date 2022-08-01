from django.db import models
from django.utils.translation import gettext_lazy as _


class GisCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True, blank=True, default=None,
    )

    class Meta:
        db_table = 'CATEGORIA_GIS'
        verbose_name = _('GIS category')
        verbose_name_plural = _('GIS categories')

    def __str__(self):
        return f'{self.name}'


class GisCatalog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('gis.GisCategory', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    class Meta:
        db_table = 'CATALOGO_GIS'
        verbose_name = _('GIS catalog')
        verbose_name_plural = _('GIS catalogs')

    def __str__(self):
        return f'{self.title}'


class GisService(models.Model):
    id = models.AutoField(primary_key=True)
    catalog = models.ForeignKey(
        'gis.GisCatalog',
        on_delete=models.CASCADE,
        related_name='services',
        null=True, blank=True, default=None,
    )
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True, default=None)

    class Meta:
        db_table = 'SERVICIO_GIS'
        verbose_name = _('GIS service')
        verbose_name_plural = _('GIS services')

    def __str__(self):
        return f'{self.name}'
