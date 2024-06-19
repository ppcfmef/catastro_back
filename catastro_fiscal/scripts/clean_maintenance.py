from apps.maintenance.models import *


def run():
    ApplicationObservationDetail.objects.filter(application__ubigeo='100704').delete()
    ApplicationLandDetail.objects.filter(application__ubigeo='100704').delete()
    ApplicationResultDetail.objects.filter(application__ubigeo='100704').delete()
    Result.objects.filter(ubigeo='100704').delete()
    Application.objects.filter(ubigeo='100704').delete()
