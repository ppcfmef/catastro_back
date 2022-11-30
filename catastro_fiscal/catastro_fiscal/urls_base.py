from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import redirect
from .swagger import schema_view

urlpatterns = [
    re_path('^$', lambda request: redirect('swagger/', permanent=False)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('catastro_fiscal.urls_api', namespace='api')),
    path('captchae/', include('apps.captchae.urls')),  # capthca urls
    path('api/captcha/', include('rest_captcha.urls')),
    path('export/', include('catastro_fiscal.urls_export', namespace='export')),
]
