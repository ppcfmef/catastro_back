from django.urls import path

from .views.lands import LandExportView

app_name = 'export_land'

urlpatterns = [
    path('records/', LandExportView.as_view())
]
