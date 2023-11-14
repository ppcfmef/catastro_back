from apps.incomes_data.models import *


def run():
    Contribuyente.objects.all().delete()
    MarcoPredio.objects.all().delete()
    Arancel.objects.all().delete()
    PredioDato.objects.all().delete()
    PredioCaracteristica.objects.all().delete()
    Recaudacion.objects.all().delete()
    Deuda.objects.all().delete()
    Emision.objects.all().delete()
    BaseImponible.objects.all().delete()
    Alicuota.objects.all().delete()
    AmnistiaContribuyente.objects.all().delete()
    AmnistiaMunicipal.objects.all().delete()
    VaremMunicipal.objects.all().delete()
