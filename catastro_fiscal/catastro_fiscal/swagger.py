from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Catastro Fiscal",
        default_version='v1',
        description="API rest para el proyecto MEF Catastro Fiscal"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
