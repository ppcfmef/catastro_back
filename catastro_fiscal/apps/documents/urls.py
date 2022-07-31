from rest_framework.routers import DefaultRouter
from .views import ManualViewSet, TutorialViewSet, FAQViewSet, CategoryViewSet

app_name = 'api_documents'

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('manuals', ManualViewSet)
router.register('tutorials', TutorialViewSet)
router.register('faq', FAQViewSet)

urlpatterns = router.urls
