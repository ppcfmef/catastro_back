from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( TicketViewSet, LocationViewSet,RecordOwnerShipViewSet)


app_name = 'api_land_inspections'
router = DefaultRouter()
router.register('ticket',TicketViewSet,basename ='ticket')
router.register('location', LocationViewSet, basename='location')
router.register('recordowner', RecordOwnerShipViewSet, basename='recordowner')
urlpatterns = router.urls