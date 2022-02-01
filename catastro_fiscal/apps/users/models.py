from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from apps.master_data.models import Institution
from apps.places.models import Department, Province, District


class Role(models.Model):
    name = models.CharField(_('name'), max_length=150)
    is_active = models.BooleanField(_('is active'), default=True)
    description = models.TextField(_('description'), blank=True, null=True)

    class Meta:
        db_table = 'ROL'

    def __str__(self):
        return self.name


class User(AbstractUser):
    """Custom user model"""
    dni = models.CharField(_('dni'), max_length=8, null=True)
    job_title = models.CharField(_('job_title'), max_length=150, blank=True, null=True)
    role = models.ForeignKey(
        Role,
        models.SET_NULL,
        verbose_name=_('role'),
        related_name='users',
        null=True
    )
    institution = models.ForeignKey(
        Institution,
        models.SET_NULL,
        verbose_name=_('institution'),
        related_name='users',
        null=True
    )
    department = models.ForeignKey(
        Department,
        models.SET_NULL,
        verbose_name=_('department'),
        related_name='users',
        null=True
    )
    province = models.ForeignKey(
        Province,
        models.SET_NULL,
        verbose_name=_('province'),
        related_name='users',
        null=True
    )
    district = models.ForeignKey(
        District,
        models.SET_NULL,
        verbose_name=_('district'),
        related_name='users',
        null=True
    )

    observation = models.TextField(_('observation'), blank=True, null=True)

    class Meta:
        db_table = 'USUARIO'

    @property
    def name(self):
        return self.get_full_name()

    @property
    def place_scope(self):
        scope = {}
        if self.district is not None:
            scope.update({'name': 'district', 'ubigeo': self.district_id})
            return scope

        if self.province is not None:
            scope.update({'name': 'province', 'ubigeo': self.province_id})
            return scope

        if self.department is not None:
            scope.update({'name': 'department', 'ubigeo': self.department_id})
            return scope

        return {'name': 'national', 'ubigeo': None}
