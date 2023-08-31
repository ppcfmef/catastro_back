from apps.lands.models import *


def run():
    UploadHistory.objects.all().delete()
    TemploralUploadRecord.objects.all().delete()
    LandOwner.objects.all().delete()
    OwnerAddress.objects.all().delete()
    Land.objects.all().delete()
    LandOwnerDetail.objects.all().delete()
    LandAudit.objects.all().delete()
