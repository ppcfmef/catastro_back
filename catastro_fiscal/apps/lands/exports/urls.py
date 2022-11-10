from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ExportRecordsView

app_name = 'api_lands_exports'

router = DefaultRouter()

urlpatterns = router.urls + [
    path('records/', ExportRecordsView.as_view())
]
