from rest_framework.routers import DefaultRouter
from .views import IncomeUploadHistoryViewset

app_name = 'api_incomes'

router = DefaultRouter()
router.register('upload', IncomeUploadHistoryViewset)

urlpatterns = router.urls
