from django.urls import re_path
from .business.views import GetBusinessView
from .persons.views import GetPersonView

app_name = 'api_integrations'

urlpatterns = [
    re_path(r'^business/(?P<document>\w+)/$', GetBusinessView.as_view()),
    re_path(r'^person/(?P<document>\w+)/$', GetPersonView.as_view())
]
