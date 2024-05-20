from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
   PhotoViewSet
)

app_name = 'api_valorization'
router = DefaultRouter()
router.register('offer/photo', PhotoViewSet, basename='offer_photo')
urlpatterns = router.urls