from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LandGapAnalisysViewSet , DistrictViewSet 
)

app_name = 'api_gap_analisys'

router = DefaultRouter()

router.register('land', LandGapAnalisysViewSet, basename='land')
router.register('district', DistrictViewSet, basename='district')
urlpatterns = router.urls