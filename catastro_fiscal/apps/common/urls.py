from rest_framework.routers import DefaultRouter
from .views import NavigationViewset

app_name = 'api_common'

router = DefaultRouter()
router.register(r'navigation', NavigationViewset)
urlpatterns = router.urls
