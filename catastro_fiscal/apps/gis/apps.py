from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GisConfig(AppConfig):
    name = 'apps.gis'
    verbose_name = _('metadata GIS')
