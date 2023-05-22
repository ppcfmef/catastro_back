from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ApplicationViewSet,LandViewSet , ResultViewSet,ApplicationObservationDetailViewSet
)

app_name = 'api_maintenance'

router = DefaultRouter()
router.register('application', ApplicationViewSet, basename='application')
router.register('land', LandViewSet, basename='land')
router.register('result', ResultViewSet, basename='result')
router.register('observation', ApplicationObservationDetailViewSet, basename='observation')
urlpatterns = router.urls