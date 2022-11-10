from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UploadHistoryViewset, LandViewSet, LandOwnerViewSet, OwnerSearchByDocumentViewset, CreateAndEditOwnerViewset,
    LandDetailViewSet, LandCreateAndEditViewset, SearchInactiveLandByCpu, SummaryRecord, LandOwnerDetailViewSet
)

app_name = 'api_lands'

router = DefaultRouter()
router.register('registry', UploadHistoryViewset)  # ToDo: cambiar por upload (carga masiva)
router.register('records/search-inactive', SearchInactiveLandByCpu)
router.register('records', LandViewSet)
router.register('owners', LandOwnerViewSet)
router.register('owners', LandOwnerDetailViewSet)
router.register('detail', LandDetailViewSet)
router.register('register', LandCreateAndEditViewset)
router.register('owners/search', OwnerSearchByDocumentViewset)
router.register('owners/register', CreateAndEditOwnerViewset)
urlpatterns = router.urls + [
    path('summary/', SummaryRecord.as_view()),
    path('exports/', include('apps.lands.exports.urls', namespace='lands_exports')),
]
