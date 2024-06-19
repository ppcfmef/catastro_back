from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    code = models.CharField(_('code'), max_length=2, primary_key=True)
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        db_table = 'DEPARTAMENTO'
        verbose_name = _('department')
        verbose_name_plural = _('departments')

    def __str__(self):
        return f'{self.code} - {self.name}'


class Province(models.Model):
    code = models.CharField(_('code'), max_length=4, primary_key=True)
    department = models.ForeignKey(
        Department,
        models.CASCADE,
        verbose_name=_('department'),
        related_name='provinces'
    )
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        db_table = 'PROVINCIA'
        verbose_name = _('province')
        verbose_name_plural = _('provinces')

    def __str__(self):
        return f'{self.code} - {self.name}'


class District(models.Model):
    code = models.CharField(_('code'), max_length=6, primary_key=True)
    province = models.ForeignKey(
        Province,
        models.CASCADE,
        verbose_name=_('province'),
        related_name='districts'
    )
    name = models.CharField(_('name'), max_length=150)
    zone = models.CharField(_('zone'), max_length=2)
    municipal_name = models.CharField( max_length=150,null=True, blank=True)
    sec_ejec =models.IntegerField( null=True, blank=True)
    class Meta:
        db_table = 'DISTRITO'
        verbose_name = _('district')
        verbose_name_plural = _('districts')

    def __str__(self):
        return f'{self.code} - {self.name}'

    @property
    def department(self):
        return getattr(self.province, 'department_id')


class PlaceScope(models.Model):
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        db_table = 'AMBITO'
        verbose_name = _('place scope')
        verbose_name_plural = _('place scopes')

    def __str__(self):
        return f'{self.name}'


class Extension(models.Model):
    ubigeo = models.ForeignKey(
        District,
        models.CASCADE,
        verbose_name=_('ubigeo'),
        related_name='extensions',
        blank=True, null=True,
    )
    x_min = models.CharField(max_length=20)
    x_max = models.CharField(max_length=20)
    y_min = models.CharField(max_length=20)
    y_max = models.CharField(max_length=20)
    x = models.CharField(max_length=20)
    y = models.CharField(max_length=20)
    id_dist = models.IntegerField(null=True)

    class Meta:
        db_table = 'UBICACION_EXTENDIDO'
        verbose_name = _('extension')
        verbose_name_plural = _('extensions')


class Resource(models.Model):
    ubigeo = models.ForeignKey(
        District,
        models.CASCADE,
        verbose_name=_('ubigeo'),
        related_name='resources',
        blank=True, null=True
    )
    source = models.CharField(_('source'), max_length=50, null=True)
    utm = models.IntegerField(_('utm'))
    gis_service = models.CharField(_('gis service'), max_length=255)

    class Meta:
        db_table = 'UBICACION_RECURSOS'
        verbose_name = _('resource')
        verbose_name_plural = _('resources')
