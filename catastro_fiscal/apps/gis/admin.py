from django.contrib import admin

from .models import GisCategory, GisCatalog, GisService


@admin.register(GisCategory)
class GisCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    list_filter = ['parent']


class GisServiceInline(admin.TabularInline):
    list_display = ['id', 'name', 'catalog']
    model = GisService
    extra = 1


@admin.register(GisCatalog)
class GisCatalogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    list_filter = ['category']
    inlines = [GisServiceInline, ]
