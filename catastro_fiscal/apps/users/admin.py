from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'), {'fields': ('institution', 'dni', 'first_name', 'last_name', 'email', 'job_title')}),
        (_('User account'), {'fields': ('role', 'username', 'password', 'is_active')}),
        (_('User scope'), {'fields': ('department', 'province', 'district')}),
        (_('Detail account'), {'fields': ('observation',)}),
    )
