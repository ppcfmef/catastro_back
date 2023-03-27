from django.contrib import admin
from .models import Navigation


@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'type', 'link', 'icon', 'order')
    list_editable = ('icon', 'order', )
