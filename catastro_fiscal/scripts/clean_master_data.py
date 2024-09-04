from apps.master_data.models import *


def run():
    MasterTipoPredio.objects.all().delete()