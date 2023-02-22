from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoricalRecordViewset, HistoricalRecordByUserViewset

app_name = 'historical_records'

router = DefaultRouter()
router.register('', HistoricalRecordViewset)
router.register('by-user', HistoricalRecordByUserViewset)
urlpatterns = router.urls
