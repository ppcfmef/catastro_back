from django.contrib import admin
from .models import UploadHistory, LandAudit


@admin.register(UploadHistory)
class UploadHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(LandAudit)
class LandAuditAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_reference', 'source', 'type', 'update_date', 'update_by')
