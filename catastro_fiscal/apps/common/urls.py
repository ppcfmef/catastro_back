from rest_framework.routers import DefaultRouter
from .views import NavigationViewset, NavigationManageViewset, NavigationViewViewset, NavigationAuthorizationViewset

app_name = 'api_common'

router = DefaultRouter()
router.register(r'navigation/manage', NavigationManageViewset)
router.register(r'navigation/view', NavigationViewViewset)
router.register(r'navigation', NavigationViewset, basename='navigation')
router.register(r'navigation/authorization', NavigationAuthorizationViewset, basename='navigation_authorization')
urlpatterns = router.urls
