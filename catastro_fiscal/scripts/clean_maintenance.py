from apps.maintenance.models import *


def run():
    ApplicationObservationDetail.objects.all().delete()
    ApplicationLandDetail.objects.all().delete()
    ApplicationResultDetail.objects.all().delete()
    Result.objects.all().delete()
    Application.objects.all().delete()
