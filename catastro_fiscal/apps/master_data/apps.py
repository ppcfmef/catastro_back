from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MasterDataConfig(AppConfig):
    name = 'apps.master_data'
    verbose_name = _('master data')
