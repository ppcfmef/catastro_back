from django.urls import path
from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token , obtain_jwt_token
from .views import CustomObtainJSONWebToken

app_name = 'external'




urlpatterns = [
    path('iniciar-sesion', CustomObtainJSONWebToken.as_view(), name='iniciar-sesion'),
    path('verificar-acceso-token', verify_jwt_token, name='verificar-acceso-token'),
    path('refrescar-acceso-token', refresh_jwt_token, name='refrescar-acceso-token')
]
