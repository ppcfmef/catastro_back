from apps.lands.models import *
from apps.historical.models import HistoricalRecord


def run():
    UploadHistory.objects.all().delete()
    TemploralUploadRecord.objects.all().delete()
    LandOwner.objects.all().delete()
    OwnerAddress.objects.all().delete()
    Land.objects.all().delete()
    LandOwnerDetail.objects.all().delete()
    LandAudit.objects.all().delete()

    # clean Historical
    HistoricalRecord.objects.all().delete()
