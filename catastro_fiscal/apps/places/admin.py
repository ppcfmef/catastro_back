from django.contrib import admin  # noqa: F401
from .models import PlaceScope, District
from import_export.admin import ImportExportModelAdmin

@admin.register(PlaceScope)
class PlaceScopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



@admin.register(District)
class MasterTipoObraComplementariaAdmin( ImportExportModelAdmin):
    list_display = ('code', 'name',)
    list_filter =('code',)
