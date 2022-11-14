from django.db.models import Count
from ..models import TemploralUploadRecord, LandOwner, Land, UploadHistory


class UploadLandService:

    def execute(self, upload_history: UploadHistory):
        self.land_owner_upload(upload_history)
        self.land_upload(upload_history)
        self.count_lands_by_owner()
        self.sumary_status_history(upload_history)

    def land_owner_upload(self, upload_history):
        # Insertar nuevos
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, owner_record_status=1)
        land_owners_bulk = []
        for temploral in temploral_records:
            land_owners_bulk.append(LandOwner(**temploral.owner_record))
        LandOwner.objects.bulk_create(land_owners_bulk)

    def land_upload(self, upload_history):
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, land_record_status=1)
        land_bulk = []
        for temploral in temploral_records:
            record = temploral.record
            land_record = temploral.land_record
            document_type = record.get('tip_doc')

            if document_type is not None and document_type != "":
                document = self.make_document(record)
                land_record.update({
                    'owner': LandOwner.objects.filter(
                        document_type=record.get('tip_doc'),
                        dni=document
                    ).first()
                })
            land_bulk.append(Land(**land_record))
        Land.objects.bulk_create(land_bulk)

        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, land_record_status=2)

        for temploral in temploral_records:
            record = temploral.record
            land_record = temploral.land_record
            document_type = record.get('tip_doc')

            if document_type is not None and document_type != "":
                document = self.make_document(record)
                land_record.update({
                    'owner': LandOwner.objects.filter(
                        document_type=record.get('tip_doc'),
                        dni=document
                    ).first()
                })
            Land.objects.filter(id=land_record.get('id')).update(**land_record)

        upload_history.status = 'LOADED'

    def make_document(self, record):
        document_type = record.get('tip_doc')
        document = record.get('doc_iden')
        ubigeo = record.get('ubigeo')
        return '-'.join([ubigeo, document]) if document_type in ['00', '08'] else document

    def count_lands_by_owner(self):
        lands = Land.objects.values('owner').annotate(number_lands=Count('owner'))
        for land in lands:
            LandOwner.objects.filter(id=land['owner']).update(number_lands=land['number_lands'])

    def sumary_status_history(self, upload_history):
        upload_history.status = 'LOADED'
        upload_history.total_land = upload_history.land_set.count()
        upload_history.total_land_mapping = upload_history.land_set.filter(status=1).count()
        upload_history.save()
