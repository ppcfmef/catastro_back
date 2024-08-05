from apps.master_data.models import *


def run():
    MasterPropertyType.objects.all().delete()