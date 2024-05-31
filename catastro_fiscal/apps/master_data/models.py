from django.db import models
from django.utils.translation import gettext_lazy as _


class Institution(models.Model):
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        db_table = 'INSTITUCION'
        verbose_name = _('institution')
        verbose_name_plural = _('institutions')

    def __str__(self):
        return self.name


class MasterDomain(models.Model):
    id = models.CharField(_('key id'), max_length=50, primary_key=True)
    name = models.CharField(_('name'), max_length=150)
    description = models.CharField(_('description'), max_length=150)
    short_name = models.CharField(_('short name'), max_length=100)
    estado = models.IntegerField(blank=True, null=True, default=1)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MasterTypeUrbanUnit(MasterDomain):
    class Meta:
        db_table = 'M_TIPO_UU'
        verbose_name = _('urban unit type')
        verbose_name_plural = _('urban unit types')


class MasterSide(MasterDomain):
    class Meta:
        db_table = 'M_LADO'
        verbose_name = _('side')
        verbose_name_plural = _('sides')


class MasterCodeStreet(MasterDomain):
    class Meta:
        db_table = 'M_COD_VIA'
        verbose_name = _('street code')
        verbose_name_plural = _('street codes')


class MasterPropertyType(MasterDomain):
    class Meta:
        db_table = 'M_TIPO_PREDIO'
        verbose_name = _('property type')
        verbose_name_plural = _('property types')


class MasterResolutionType(MasterDomain):
    class Meta:
        db_table = 'M_TDOC_RES'
        verbose_name = _('resolution type')
        verbose_name_plural = _('resolution types')

class MasterTipoDocumentoIdentidad(MasterDomain):
    class Meta:
        db_table = 'M_TDOC_IDENTIDAD'
        verbose_name = _('tipo de documento de identidad')
        verbose_name_plural = _('tipos de documento de identidad')


class MasterType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(_('name'), max_length=150,blank=True, null=True)
    description = models.CharField(_('description'), max_length=150)
    short_name = models.CharField(_('short name'), max_length=100)
    estado = models.IntegerField(blank=True, null=True, default=1)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class MasterTipoContribuyente(MasterType):
    class Meta:
        db_table = 'M_TIPO_CONTRIBUYENTE'
        verbose_name = _('tipo de contribuyente')
        verbose_name_plural = _('tipos de contribuyente')

class MasterTipoPropiedad(MasterType):
    class Meta:
        db_table = 'M_TIPO_PROPIEDAD'
        verbose_name = _('tipo de propiedad')
        verbose_name_plural = _('tipos de propiedad')


class MasterTipoTransferencia(MasterType):
    class Meta:
        db_table = 'M_TIPO_TRANSFERENCIA'
        verbose_name = _('tipo de transferencia')
        verbose_name_plural = _('tipos de transferencia')


class MasterTipoUsoPredio(MasterType):
    class Meta:
        db_table = 'M_TIPO_USO_PREDIO'
        verbose_name = _('tipo uso de predio')
        verbose_name_plural = _('tipo uso de predio')