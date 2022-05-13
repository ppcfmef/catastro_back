from rest_framework.routers import DefaultRouter
from .views import UploadHistoryViewset

app_name = 'api_lands'

router = DefaultRouter()
router.register('registry', UploadHistoryViewset)

urlpatterns = router.urls
