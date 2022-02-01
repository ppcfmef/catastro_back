from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    code = models.CharField(_('code'), max_length=2, primary_key=True)
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        db_table = 'DEPARTAMENTO'

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

    class Meta:
        db_table = 'DISTRITO'

    def __str__(self):
        return f'{self.code} - {self.name}'
