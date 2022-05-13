import openpyxl
from .models import UploadHistory, TemploralUploadRecord


class ReadXlsService:
    def __init__(self, file):
        self.file = file
        self.headers = []

    def read(self):
        datos = []
        wb = openpyxl.load_workbook(self.file)
        ws = wb.worksheets[0]

        for row in ws.rows:
            for cell in row:
                self.headers.append(str(cell.value).strip().lower().replace(' ', '_'))
            break

        header_range = range(len(self.headers))

        for row in ws.iter_rows(min_row=2):
            record = []
            for i in header_range:
                record.append((self.headers[i], row[i].value))
            datos.append(dict(record))

        return datos


class UploadLandRecordService:

    read_file_service = ReadXlsService

    def read(self, upload_history):
        return self.read_file_service(file=upload_history.file_upload.file).read()

    def execute(self, upload_history: UploadHistory):
        records = self.read(upload_history)
        temploral_upload_record_bulk = []
        for record in records:
            tmp_upload_record = TemploralUploadRecord(record=record, upload_history=upload_history, status='OK_NEW')
            temploral_upload_record_bulk.append(tmp_upload_record)
        TemploralUploadRecord.objects.bulk_create(temploral_upload_record_bulk)
