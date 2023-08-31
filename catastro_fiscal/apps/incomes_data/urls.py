from rest_framework.routers import DefaultRouter
from .views import (
    IncomeUploadHistoryViewset, IncomeUploadStatusViewSet, RTContribuyenteViewSet, RTMarcoPredioViewSet,
    RTArancelViewSet, RTPredioDatoViewSet, RTPredioCaracteristicaViewSet, RTRecaudacionViewSet,
    RTDeudaViewSet, RTEmisionViewSet, RTBaseImponibleViewSet, RTAlicuotaViewSet,
    RTAmnistiaContribuyenteViewSet, RTAmnistiaMunicipalViewSet, RTVaremMunicipalViewSet
)

app_name = 'api_incomes'

router = DefaultRouter()
router.register('rtcontribuyente', RTContribuyenteViewSet)
router.register('rtmarcopredio', RTMarcoPredioViewSet)
router.register('rtarancel', RTArancelViewSet)
router.register('rtpediodato', RTPredioDatoViewSet)
router.register('rtprediocaracteristica', RTPredioCaracteristicaViewSet)
router.register('rtrecaudacion', RTRecaudacionViewSet)
router.register('rtdeuda', RTDeudaViewSet)
router.register('rtemision', RTEmisionViewSet)
router.register('rtbaseimponible', RTBaseImponibleViewSet)
router.register('rtalicuota', RTAlicuotaViewSet)
router.register('rtamnistiacontribuyente', RTAmnistiaContribuyenteViewSet)
router.register('rtamnistiamunicipal', RTAmnistiaMunicipalViewSet)
router.register('rtvaremmunicipal', RTVaremMunicipalViewSet)
router.register('upload', IncomeUploadHistoryViewset)
router.register('upload/status', IncomeUploadStatusViewSet)

urlpatterns = router.urls
