from rest_framework import exceptions, serializers
from apps.lands.models import UploadHistory, TemploralUploadRecord
from apps.lands.services.upload_temporal import AbstractUploadTemporal


class IncomeUploadTemporalService(AbstractUploadTemporal):
    valid_serializer = None

    def execute(self, upload_history: UploadHistory):
        records = self.read(upload_history)
        upload_history = self.update_ubigeo(upload_history, records)
        self.validate_header(records, raise_exception=True)
        self.upload(upload_history, records)
        self.loaded(upload_history)

    def mapper(self):
        return {}

    def file_header(self):
        return list(self.mapper().values())

    def validate_header(self, records, raise_exception=False):
        record = records[0]
        headers = set(self.file_header())
        headers_in = set(list(record.keys()))

        valid_headers = headers.issubset(headers_in)

        if raise_exception and not valid_headers:
            raise exceptions.ValidationError("El archivo no tiene el formato valido")

        return valid_headers

    def upload(self, upload_history, records):
        data = []
        status, error_code = 'OK_NEW', 'OK'
        error_message = ''

        for record in records:
            record = self._map_record(upload_history, record)
            serializer = self.valid_serializer(data=record)
            if not serializer.is_valid():
                status, error_code = 'ERROR', 'NOT_VALID'
                error_message = serializer.errors

            temporal_upload = self._make_tmp_upload_record(
                upload_history, record,
                status=status,
                error_code=error_code,
                error_message=error_message
            )
            data.append(temporal_upload)

        TemploralUploadRecord.objects.bulk_create(data)

    def loaded(self, upload_history):
        UploadHistory.objects.filter(id=upload_history.id, status='IN_PROGRESS_TMP') \
            .update(status='LOADED_TMP')

    def _map_record(self, upload_history, record):
        land_mappers = self.mapper()
        if 'ubigeo' in land_mappers:
            ubigeo = upload_history.ubigeo_id
            record.update({'ubigeo': ubigeo})
        return {key: record.get(value) for key, value in land_mappers.items()}

    def _make_tmp_upload_record(self, upload_history, record, **kwargs):
        status = kwargs.get('status', 'OK_NEW')
        error_code = kwargs.get('error_code', 'ERROR')
        error_message = kwargs.get('error_message', '')

        if status == 'ERROR':
            error_record = kwargs.get('error_record', record)
        else:
            error_record = kwargs.get('error_record', {})

        return TemploralUploadRecord(
            record=record,
            error_record=error_record,
            upload_history=upload_history,
            status=status,
            error_code=error_code,
            error_message=error_message
        )
