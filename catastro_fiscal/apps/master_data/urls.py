from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import InstitutionViewSet, MasterDomainView

app_name = 'api_master'

router = DefaultRouter()
router.register(r'institution', InstitutionViewSet)

urlpatterns = [
    path('domain/', MasterDomainView.as_view())
] + router.urls
