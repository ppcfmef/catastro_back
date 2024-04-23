from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Photo , PhotoType

@admin.register(Photo)
class PhotoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

@admin.register(PhotoType)
class PhotoTypeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass