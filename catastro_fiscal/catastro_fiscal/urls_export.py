from django.urls import include, path

app_name = 'export'

urlpatterns = [
    path('land/', include('apps.lands.exports.urls', namespace='export_land')),
]
