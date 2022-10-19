from django.contrib import admin  # noqa: F401
from import_export.admin import ImportExportModelAdmin
from .models import *


class MasterAdminMixin:
    list_display = ('id', 'name')


@admin.register(MasterTypeUrbanUnit)
class MasterTypeUrbanUnitAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterSide)
class MasterSideAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterCodeStreet)
class MasterCodeStreetAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterPropertyType)
class MasterPropertyTypeAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(MasterResolutionType)
class MasterResolutionTypeAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass


@admin.register(Institution)
class InstitutionAdmin(MasterAdminMixin, ImportExportModelAdmin):
    pass
