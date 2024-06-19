from apps.lands.models import *
from apps.historical.models import HistoricalRecord


def run():
    Domicilio.objects.filter(ubigeo='100704').delete()
    UploadHistory.objects.filter(ubigeo='100704').delete()
    TemploralUploadRecord.objects.all().delete()
    LandOwner.objects.filter(ubigeo='100704').delete()
    OwnerAddress.objects.filter(ubigeo='100704').delete()
    Land.objects.filter(ubigeo='100704').delete()
    LandOwnerDetail.objects.filter(ubigeo='100704').delete()
    LandAudit.objects.filter(ubigeo='100704').delete()

    # clean Historical
    HistoricalRecord.objects.all().delete()
