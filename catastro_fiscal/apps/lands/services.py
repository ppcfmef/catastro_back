import openpyxl
from django.db.models import Count
from .models import UploadHistory, TemploralUploadRecord, Land, LandOwner


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

    def temporal_upload(self, upload_history, records):
        temploral_upload_record_bulk = []
        for record in records:
            tmp_upload_record = TemploralUploadRecord(record=record, upload_history=upload_history, status='OK_NEW')
            temploral_upload_record_bulk.append(tmp_upload_record)
        TemploralUploadRecord.objects.bulk_create(temploral_upload_record_bulk)

    def land_upload(self, upload_history):
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, status='OK_NEW')
        self.land_owner_upload(temploral_records)
        land_bulk = []
        for temploral in temploral_records:
            record = temploral.record
            land = Land(
                cup=record.get('cod_pre'),
                cpm=record.get('cod_cpu'),
                habilitacion_name=record.get('nom_uu'),
                steet_name=record.get('nom_via'),
                urban_mza=record.get('mzn_urb'),
                urban_lot_number=record.get('lot_urb'),
                site=None,
                municipal_number=None,
                dpto_number=None,
                indoor=record.get('interior'),
                block=record.get('block'),
                latitude=record.get('coor_y'),
                longitude=record.get('coor_x'),
                land_area=record.get('area_terreno'),
                built_area=None,
                owner=LandOwner.objects.filter(dni=record.get('doc_iden')).first()
            )
            land_bulk.append(land)
        Land.objects.bulk_create(land_bulk)

    def land_owner_upload(self, temploral_records):
        land_owners_bulk = []
        for temploral in temploral_records:
            record = temploral.record
            land_owner = LandOwner(
                code=record.get('cod_contr'),
                document_type=record.get('tip_doc'),
                dni=record.get('doc_iden'),
                name=record.get('nombre'),
                paternal_surname=record.get('ap_pat'),
                maternal_surname=record.get('ap_mat'),
                tax_address=record.get('dir_fiscal'),
            )
            land_owners_bulk.append(land_owner)
        LandOwner.objects.bulk_create(land_owners_bulk)

    def count_lands_by_owner(self):
        lands = Land.objects.values('owner').annotate(number_lands=Count('owner'))
        for land in lands:
            LandOwner.objects.filter(id=land['owner']).update(number_lands=land['number_lands'])

    def execute(self, upload_history: UploadHistory):
        records = self.read(upload_history)
        self.temporal_upload(upload_history, records)
        self.land_upload(upload_history)
        self.count_lands_by_owner()
