from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('auth/', include('apps.users.url_auth', namespace='api_auth')),
    path('users/', include('apps.users.urls', namespace='api_user')),
    path('common/', include('apps.common.urls', namespace='api_common')),
]
