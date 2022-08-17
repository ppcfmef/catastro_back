from rest_framework.routers import DefaultRouter

from .views import GisCategoryViewSet, GisCatalogViewSet, GisServiceViewSet

app_name = 'api_gis'

router = DefaultRouter()
router.register('categories', GisCategoryViewSet)
router.register('catalogs', GisCatalogViewSet)
router.register('services', GisServiceViewSet)

urlpatterns = router.urls
