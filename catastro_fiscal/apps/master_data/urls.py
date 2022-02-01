from rest_framework.routers import DefaultRouter
from .views import InstitutionViewSet

app_name = 'api_master'

router = DefaultRouter()
router.register(r'institution', InstitutionViewSet)

urlpatterns = router.urls
