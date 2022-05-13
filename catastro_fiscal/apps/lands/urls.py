from rest_framework.routers import DefaultRouter
from .views import UploadHistoryViewset, LandViewSet, LandOwnerViewSet

app_name = 'api_lands'

router = DefaultRouter()
router.register('registry', UploadHistoryViewset)
router.register('records', LandViewSet)
router.register('owners', LandOwnerViewSet)

urlpatterns = router.urls
