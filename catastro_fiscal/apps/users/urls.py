from django.urls import path
from .views import UserProfileShortView

app_name = 'api_user'

urlpatterns = [
    path('user/', UserProfileShortView.as_view())
]
