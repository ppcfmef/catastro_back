from django.contrib import admin

from .models import Document, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    list_filter = ['parent']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', 'category']
    list_filter = ['type', 'category']
