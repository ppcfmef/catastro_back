from django.urls import re_path
from .business.views import GetBusinessView
from .persons.views import GetPersonView
from .land_owner.views import GetLandOwnerView

app_name = 'api_integrations'

urlpatterns = [
    re_path(r'^business/(?P<document>\w+)/$', GetBusinessView.as_view()),
    re_path(r'^person/(?P<document>\w+)/$', GetPersonView.as_view()),
    re_path(r'^land-owner/(?P<ubigeo>\w+)/(?P<land_owner>\w+)/$', GetLandOwnerView.as_view()),
]
