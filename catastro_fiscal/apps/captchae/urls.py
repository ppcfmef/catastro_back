from django.urls import path
from . import views

app_name = 'captchae'
urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.RestCaptchaView.as_view(), name='rest_captcha-view'),
]