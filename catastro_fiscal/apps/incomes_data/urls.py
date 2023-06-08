from rest_framework.routers import DefaultRouter
from .views import (
    IncomeUploadHistoryViewset, IncomeUploadStatusViewSet, RTContribuyenteViewSet, RTMarcoPredioViewSet,
    RTArancelViewSet, RTPredioDatoViewSet
)

app_name = 'api_incomes'

router = DefaultRouter()
router.register('upload', IncomeUploadHistoryViewset)
router.register('upload/status', IncomeUploadStatusViewSet)
router.register('rtcontribuyente', RTContribuyenteViewSet)
router.register('rtmarcopredio', RTMarcoPredioViewSet)
router.register('rtarancel', RTArancelViewSet)
router.register('rtpediodato', RTPredioDatoViewSet)

urlpatterns = router.urls
