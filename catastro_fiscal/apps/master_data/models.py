from django.db import models
from django.utils.translation import gettext_lazy as _


class Institution(models.Model):
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        db_table = 'INSTITUCION'

    def __str__(self):
        return self.name


class MasterDomain(models.Model):
    id = models.CharField(_('key id'), max_length=50, primary_key=True)
    name = models.CharField(_('name'), max_length=150)
    description = models.CharField(_('description'), max_length=150)
    short_name = models.CharField(_('short name'), max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MasterTypeUrbanUnit(MasterDomain):
    class Meta:
        db_table = 'M_TIPO_UU'
        verbose_name = _('Type Urban Unit')
        verbose_name_plural = _('Type Urban Unit')


class MasterSide(MasterDomain):
    class Meta:
        db_table = 'M_LADO'
        verbose_name = _('Side')
        verbose_name_plural = _('Side')


class MasterCodeStreet(MasterDomain):
    class Meta:
        db_table = 'M_COD_VIA'
        verbose_name = _('Code Street')
        verbose_name_plural = _('Code Street')


class MasterPropertyType(MasterDomain):
    class Meta:
        db_table = 'M_TIPO_PREDIO'
        verbose_name = _('Property Type')
        verbose_name_plural = _('Property Type')
