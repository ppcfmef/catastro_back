from django.urls import path
from . import views

app_name = 'captchae'
urlpatterns = [
    path('api/', views.RestCaptchaView.as_view(), name='rest_captcha-view'),
]
