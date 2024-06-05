from django.contrib import admin
from .models import UploadHistory, LandAudit,Land,Contacto,TipoMedioContacto


@admin.register(UploadHistory)
class UploadHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(LandAudit)
class LandAuditAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_reference', 'source_change', 'type', 'update_date', 'update_by')

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ('ubigeo', 'cpm', 'cup')
    list_filter = ["ubigeo"]
    search_fields  = ['ubigeo']

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoMedioContacto)
class TipoMedioContactoAdmin(admin.ModelAdmin):
    pass

