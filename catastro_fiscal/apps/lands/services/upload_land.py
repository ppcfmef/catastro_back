from django.db.models import Count
from ..models import TemploralUploadRecord, LandOwner, Land, UploadHistory, LandOwnerDetail


class UploadLandService:

    def execute(self, upload_history: UploadHistory):
        self.land_owner_upload(upload_history)
        self.land_upload(upload_history)
        self.land_owner_detail_upload(upload_history)
        self.count_lands_by_owner(upload_history)
        self.sumary_status_history(upload_history)

    def land_owner_upload(self, upload_history):
        # Insertar nuevos
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, owner_record_status=1)
        land_owners_bulk = [LandOwner(**temploral.owner_record) for temploral in temploral_records]
        LandOwner.objects.bulk_create(land_owners_bulk)
        # Se deben actualizar datos del contribuyente
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, owner_record_status=2)
        for temporal in temploral_records:
            id = temporal.owner_record.get('id', None)
            if id is None:
                continue
            clean_record = self._clean_record(record=temporal.owner_record)
            LandOwner.objects.filter(id=id).update(**clean_record)

    def _clean_record(self, record):
        clean_record = {}
        for k, v in record.items():
            if not (v is None or str(v).strip('') == ''):
                clean_record.update({k: v})
        return clean_record

    def land_upload(self, upload_history):
        # Insetamos los nuevos registros
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, land_record_status=1)
        land_bulk = [Land(**temploral.land_record) for temploral in temploral_records]
        Land.objects.bulk_create(land_bulk)

        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, land_record_status=2)
        # Actualizar registros del maestro de predios
        for temporal in temploral_records:
            id = temporal.land_record.get('id', None)
            if id is None:
                continue
            clean_record = self._clean_record(record=temporal.land_record)
            Land.objects.filter(id=id).update(**clean_record)

    def land_owner_detail_upload(self, upload_history):
        Land_owner_detail_bulk = []
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history).exclude(status='ERROR')
        ubigeo = upload_history.ubigeo
        for temporal in temploral_records:
            land_id = temporal.land_record.get('id', None)
            owner_id = temporal.owner_record.get('id', None)
            cpm = temporal.land_record.get('cpm', None)
            owner_code = temporal.owner_record.get('code', None)

            if land_id is None and cpm is not None:
                land_id = Land.objects.filter(ubigeo=ubigeo, cpm=cpm).values('id').first().get('id', None)

            if owner_id is None and owner_code is not None:
                owner_id = LandOwner.objects.filter(ubigeo=ubigeo, code=owner_code).values('id').first().get('id', None)

            if land_id is None or owner_id is None:
                continue

            if LandOwnerDetail.objects.filter(land_id=land_id, owner_id=owner_id).exists():
                continue

            Land_owner_detail_bulk.append(LandOwnerDetail(ubigeo=ubigeo, land_id=land_id, owner_id=owner_id))
        LandOwnerDetail.objects.bulk_create(Land_owner_detail_bulk)

    def count_lands_by_owner(self, upload_history):
        for landowner in upload_history.landowner_set.all():
            number_lands = LandOwnerDetail.objects.filter(owner_id=landowner.id).count()
            LandOwner.objects.filter(id=landowner.id).update(number_lands=number_lands)

    def sumary_status_history(self, upload_history):
        upload_history.status = 'LOADED'
        upload_history.total_land = upload_history.land_set.count()
        upload_history.total_land_mapping = upload_history.land_set.filter(status=1).count()
        upload_history.save()
