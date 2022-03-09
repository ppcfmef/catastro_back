from django.contrib import admin  # noqa: F401
from .models import PlaceScope


@admin.register(PlaceScope)
class PlaceScopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
