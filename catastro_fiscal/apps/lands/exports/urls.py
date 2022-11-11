from django.urls import path

from .views.lands import LandExportView
from .views.temporal_upload_records import TemporalUploadRecordExportView

app_name = 'export_land'

urlpatterns = [
    path('records/', LandExportView.as_view()),
    path('uploads/<int:upload_history>/', TemporalUploadRecordExportView.as_view()),
]
