from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UploadHistoryViewset, LandViewSet, LandOwnerViewSet, OwnerSearchByDocumentViewset, CreateAndEditOwnerViewset,
    LandDetailViewSet, LandCreateAndEditViewset, SearchInactiveLandByCpu, SummaryRecord, LandOwnerDetailViewSet,
    UploadStatusViewSet, UploadHistorySummaryViewSet
)

app_name = 'api_lands'

router = DefaultRouter()
router.register('registry', UploadHistoryViewset)  # ToDo: cambiar por upload (carga masiva)
router.register('upload/status', UploadStatusViewSet)
router.register('upload/summary', UploadHistorySummaryViewSet)
router.register('records/search-inactive', SearchInactiveLandByCpu)
router.register('records', LandViewSet, basename='lands_records')
router.register('owners/register', CreateAndEditOwnerViewset, basename='owners_register')
router.register('owners', LandOwnerViewSet, basename='owners_records')
router.register('owners', LandOwnerDetailViewSet, basename='owners')
router.register('detail', LandDetailViewSet, basename='lands')
router.register('register', LandCreateAndEditViewset, basename='lands_register')
router.register('owners/search', OwnerSearchByDocumentViewset, basename='owners_search')
urlpatterns = router.urls + [
    path('summary/', SummaryRecord.as_view()),
    path('exports/', include('apps.lands.exports.urls', namespace='lands_exports')),
]
