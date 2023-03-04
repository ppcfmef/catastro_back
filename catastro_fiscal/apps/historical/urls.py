from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoricalRecordViewset, HistoricalRecordByUserViewset

app_name = 'historical_records'

router = DefaultRouter()
router.register('by-user', HistoricalRecordByUserViewset)
router.register('', HistoricalRecordViewset)
urlpatterns = router.urls
