from apps.lands.models import UploadHistory, TemploralUploadRecord
from ..models import (
    Contribuyente, MarcoPredio, Arancel, PredioDato, PredioCaracteristica, Recaudacion, Deuda, Emision, BaseImponible
)


class IncomeUploadService:

    record_class = None

    def execute(self, upload_history: UploadHistory):
        self.clean()
        self.upload(upload_history)
        self.loaded(upload_history)

    def clean(self):
        self.record_class.objects.all().delete()

    def upload(self, upload_history: UploadHistory):
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, status='OK_NEW')
        record_bulk = [self.record_class(**temploral.record) for temploral in temploral_records]
        self.record_class.objects.bulk_create(record_bulk)

    def loaded(self, upload_history: UploadHistory):
        UploadHistory.objects.filter(id=upload_history.id).update(status='LOADED')


class RTContribuyenteUploadService(IncomeUploadService):
    record_class = Contribuyente


class RTMarcoPredioUploadService(IncomeUploadService):
    record_class = MarcoPredio


class RTArancelUploadService(IncomeUploadService):
    record_class = Arancel


class RTPredioDatoUploadService(IncomeUploadService):
    record_class = PredioDato


class RTPredioCaracteristicaUploadService(IncomeUploadService):
    record_class = PredioCaracteristica


class RTRecaudacionUploadService(IncomeUploadService):
    record_class = Recaudacion


class RTDeudaUploadService(IncomeUploadService):
    record_class = Deuda


class RTEmisionUploadService(IncomeUploadService):
    record_class = Emision


class RTBaseImponibleUploadService(IncomeUploadService):
    record_class = BaseImponible
