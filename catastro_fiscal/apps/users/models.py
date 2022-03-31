from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from core.models import AbstractAudit
from apps.common.models import Navigation
from apps.master_data.models import Institution
from apps.places.models import Department, Province, District, PlaceScope


class PermissionType(models.Model):
    code = models.CharField(_('code'), max_length=20, primary_key=True)
    description = models.CharField(_('description'), max_length=50)
    order = models.PositiveSmallIntegerField(_('order'))

    class Meta:
        db_table = 'TIPO_PERMISO'
        ordering = ['order']

    def __str__(self):
        return self.description


class Permission(models.Model):
    description = models.CharField(_('description'), max_length=50)

    class Meta:
        db_table = 'PERMISO'

    def __str__(self):
        return self.description


class Role(models.Model):
    name = models.CharField(_('name'), max_length=150)
    is_active = models.BooleanField(_('is active'), default=True)
    description = models.TextField(_('description'), blank=True, null=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissions'),
        through='RolePermission'
    )

    class Meta:
        db_table = 'ROL'

    def __str__(self):
        return self.name


class User(AbstractUser):
    """Custom user model"""
    dni = models.CharField(_('dni'), max_length=8, null=True)
    avatar = models.ImageField(_('avatar'), upload_to='users/user', null=True)
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
    place_scope = models.ForeignKey(
        PlaceScope,
        models.SET_NULL,
        verbose_name=_('user place scope'),
        related_name='users',
        null=True
    )
    department = models.ForeignKey(
        Department,
        models.SET_NULL,
        verbose_name=_('department'),
        related_name='users',
        blank=True, null=True
    )
    province = models.ForeignKey(
        Province,
        models.SET_NULL,
        verbose_name=_('province'),
        related_name='users',
        blank=True, null=True
    )
    district = models.ForeignKey(
        District,
        models.SET_NULL,
        verbose_name=_('district'),
        related_name='users',
        blank=True, null=True
    )

    observation = models.TextField(_('observation'), blank=True, null=True)

    class Meta:
        db_table = 'USUARIO'

    @property
    def name(self):
        return self.get_full_name()

    @property
    def ubigeo(self):
        if self.district is not None:
            return self.district_id

        if self.province is not None:
            return self.province_id

        if self.department is not None:
            return self.department_id

        return None

    def save(self, *args, **kwargs):
        if self.place_scope is None:
            self.set_place_scope()
        super(User, self).save(*args, **kwargs)

    def set_place_scope(self):
        if self.department is None and self.province is None and self.district is None:
            self.place_scope_id = 1
        elif self.department and self.province is None and self.district is None:
            self.place_scope_id = 2
        elif self.department and self.province and self.district is None:
            self.place_scope_id = 3
        else:
            self.place_scope_id = 4


class PermissionNavigation(AbstractAudit):
    permission = models.ForeignKey(
        Permission,
        models.CASCADE,
        verbose_name=_('permission'),
        related_name='permissions'
    )
    type = models.ForeignKey(
        PermissionType,
        models.CASCADE,
        verbose_name=_('permission type'),
        related_name='permissions'
    )
    navigation_view = models.ForeignKey(
        Navigation,
        models.CASCADE,
        verbose_name=_('navigation view'),
        related_name='permissions'
    )

    class Meta:
        db_table = 'PERMISO_NAVEGACION'

    def __str__(self):
        return f'{self.permission.description} | {self.type.description} | {self.navigation_view.title}'


class RolePermission(AbstractAudit):
    role = models.ForeignKey(
        Role,
        models.CASCADE,
        verbose_name=_('role')
    )
    permission = models.ForeignKey(
        Permission,
        models.CASCADE,
        verbose_name=_('permission')
    )

    class Meta:
        db_table = 'ROL_PERMISO'

    def __str__(self):
        return f'{self.role.name} | {self.permission.description}'
