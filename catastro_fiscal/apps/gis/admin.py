from django.contrib import admin

from .models import GisCategory, GisCatalog, GisService


@admin.register(GisCategory)
class GisCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    list_filter = ['parent']


@admin.register(GisCatalog)
class GisCatalogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    list_filter = ['category']


@admin.register(GisService)
class GisServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'catalog']
    list_filter = ['catalog']
