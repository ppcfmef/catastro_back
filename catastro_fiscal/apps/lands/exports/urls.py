from django.urls import path

from .views import ExportRecordsView

app_name = 'export_land'

urlpatterns = [
    path('records/', ExportRecordsView.as_view())
]
