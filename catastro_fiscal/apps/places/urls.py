from rest_framework.routers import DefaultRouter
from .views import DepartmentSelectViewSet, ProvinceSelectViewSet, DistrictSelectViewSet

app_name = 'api_places'

router = DefaultRouter()
router.register(r'department', DepartmentSelectViewSet)
router.register(r'province', ProvinceSelectViewSet)
router.register(r'district', DistrictSelectViewSet)

urlpatterns = router.urls
