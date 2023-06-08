from apps.lands.models import UploadHistory, TemploralUploadRecord
from ..models import Contribuyente


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
