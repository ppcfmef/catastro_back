from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('auth/', include('apps.users.url_auth', namespace='api_auth')),
    path('users/', include('apps.users.urls', namespace='api_user')),
    path('common/', include('apps.common.urls', namespace='api_common')),
    path('places/', include('apps.places.urls', namespace='api_places')),
    path('master/', include('apps.master_data.urls', namespace='api_master')),
    path('lands/', include('apps.lands.urls', namespace='api_lands')),
    path('documents/', include('apps.documents.urls', namespace='api_documents')),
    path('gis/', include('apps.gis.urls', namespace='api_gis')),
    path('integrations/', include('apps.integrations.urls', namespace='api_integrations')),
    path('historical-records/', include('apps.historical.urls', namespace='historical_records')),
    path('maintenance/', include('apps.maintenance.urls', namespace='api_maintenance')),
    path('incomes/', include('apps.incomes_data.urls', namespace='api_incomes')),
    path('mobile/', include('apps.mobile.urls', namespace='api_mobile')),
    path('gap-analisys/', include('apps.gap_analisys.urls', namespace='api_gap_analisys')),
    path('inspection/', include('apps.land_inspections.urls', namespace='land_inspections')),
    path('valorization/', include('apps.valorization.urls', namespace='valorization')),
]
