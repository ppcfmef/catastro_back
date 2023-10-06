from django.db.models import Q
from rest_framework import exceptions
from apps.places.models import District
from apps.users.models import User
from ..models import UploadHistory, TemploralUploadRecord, Land, LandOwner
from core.utils.read_xlsx import ReadXlsxService


class AbstractUploadTemporal:
    read_file_service = ReadXlsxService
    ubigeo = None

    def read(self, upload_history):
        return self.read_file_service(file=upload_history.file_upload.file).read()

    def update_ubigeo(self, upload_history, records):
        """ Validar ubigeo carga y actualizarlo en UploadHistory
            - Utilizar el primer registro del archivo cargado
            - Valida que el ubigeo exista (no sea vacio onulo)
            - Valida que el ubigeo exista en la tabla Distritos
            - valida que el ubigeo pertenesca al usuario que tiene permisos
            - Actualiza el ubigeo de UploadHistory

            Retornar la instalacion de UploadHistory Actualizada
        """
        qs = UploadHistory.objects.filter(id=upload_history.id)
        if len(records) == 0:
            qs.update(status='ERROR')
            raise exceptions.ValidationError("El archivo no tiene registros para cargar")

        record = records[0]
        self.ubigeo = str(record.get('ubigeo')).strip()

        if self.ubigeo is None or str(self.ubigeo).strip() == '':
            qs.update(status='ERROR')
            raise exceptions.ValidationError("El ubigeo no es valido")

        if not District.objects.filter(code=self.ubigeo).exists():
            qs.update(status='ERROR')
            raise exceptions.ValidationError("El ubigeo no es valido")

        # validar ubigeo del usuario

        user = User.objects.filter(username=upload_history.username).first()
        if not user:
            raise exceptions.ValidationError("El usuario no existe")

        if not user.valid_scope_ubigeo(self.ubigeo):
            raise exceptions.ValidationError("El usuario no tiene pertenece al ubigeo cargado")

        qs.update(ubigeo_id=self.ubigeo, status='IN_PROGRESS_TMP')
        return UploadHistory.objects.filter(id=upload_history.id).first()

    def get_temporal_summary(self, upload_history):
        upload_history = UploadHistory.objects.get(id=upload_history.id)
        temporal_records = TemploralUploadRecord.objects.filter(upload_history=upload_history)
        errors_data = temporal_records.filter(status='ERROR')
        corrects_data = temporal_records.filter(status__in=['OK_NEW', 'OK_OLD'])
        return {
            'upload_history_id': upload_history.id,
            'type_upload': upload_history.type_upload,
            'status': upload_history.status,
            'total': temporal_records.count(),
            'errors': errors_data.count(),
            'corrects': corrects_data.count(),
            'new': temporal_records.filter(status='OK_NEW').count(),
            'updates': temporal_records.filter(status='OK_OLD').count(),
            'errors_data': errors_data.values('record', 'error_code', 'status'),
            'corrects_data': corrects_data.values('record', 'status'),
        }


class UploadTemporalService(AbstractUploadTemporal):

    def execute(self, upload_history: UploadHistory):
        try:
            records = self.read(upload_history)
            upload_history = self.update_ubigeo(upload_history, records)
            self.cancel_last_upload(upload_history)
            self.temporal_upload(upload_history, records)
            self.loaded_temporal(upload_history)
        except Exception as e:
            upload_history.status = 'ERROR'
            upload_history.save()

    def _validate_empty_field(self, field):
        return field is not None and str(field).strip('') is not ''

    def _valid_ubigeo(self, ubigeo):
        return self._validate_empty_field(field=ubigeo) and ubigeo == self.ubigeo

    def _make_tmp_upload_record(self, upload_history, record, **kwargs):
        land_record = kwargs.get('land_record', {})
        land_record_status = kwargs.get('land_record_status', 0)
        owner_record = kwargs.get('owner_record', {})
        owner_record_status = kwargs.get('owner_record_status', 0)
        error_code = kwargs.get('error_code', 'ERROR')
        status = kwargs.get('status', None)
        if status is None:
            if land_record_status == 1:
                status = 'OK_NEW'
            elif land_record_status == 2:
                status = 'OK_OLD'
            elif land_record_status == 0 and owner_record_status != 0:
                status = 'OK_NEW'
            else:
                status = 'ERROR'

        if status == 'ERROR':
            error_record = kwargs.get('error_record', record)
        else:
            error_record = kwargs.get('error_record', {})

        return TemploralUploadRecord(
            record=record,
            error_record=error_record,
            land_record=land_record,
            land_record_status=land_record_status,
            owner_record=owner_record,
            owner_record_status=owner_record_status,
            upload_history=upload_history,
            status=status,
            error_code=error_code,
        )

    def _map_land_record(self, upload_history, record):
        land_mappers = self.land_mapper()
        land_record = {key: record.get(value) for key, value in land_mappers.items()}
        land_record.update({
            'upload_history_id': upload_history.id,
            'source': 'carga_masiva'
        })
        longitude = record.get('coord_x')
        latitude = record.get('coord_x')
        land_record.update({'status': int(longitude is not None and latitude is not None)})
        return land_record

    def temporal_upload(self, upload_history, records):
        temploral_upload_record_bulk = []
        records_unique = []
        land_records_unique = []
        owner_records_unique = []

        for record in records:
            land_record_status = 0
            owner_record_status = 0
            ubigeo = record.get('ubigeo')
            cpm = record.get('cod_pre')
            owner_code = record.get('cod_contr')

            # Validar ubigeo
            if not self._valid_ubigeo(ubigeo):
                temploral_upload_record_bulk.append(
                    self._make_tmp_upload_record(upload_history, record, error_code='IS_REQUIRED[ubigeo]')
                )
                continue

            # Validar predio
            if not self._validate_empty_field(field=cpm):
                temploral_upload_record_bulk.append(
                    self._make_tmp_upload_record(upload_history, record, error_code='IS_REQUIRED[cod_pre]')
                )
                continue

            # Generar registro de predio
            land_key = '_'.join([ubigeo, cpm])
            land_item = Land.objects.filter(ubigeo=ubigeo, cpm=cpm).first()
            land_record = self._map_land_record(upload_history, record)

            if land_item:
                land_record_status = 2
                land_record.update({
                    'id': land_item.id,
                })
            elif land_key not in land_records_unique:
                land_record_status = 1
                land_records_unique.append(land_key)
            else:
                land_record_status = 0

            # Validar que exista el contribuyente
            if not self._validate_empty_field(field=owner_code):
                tmp_upload_record = self._make_tmp_upload_record(
                    upload_history, record,
                    land_record=land_record,
                    land_record_status=land_record_status,
                    error_code='WARNING[cod_contr_empty]'
                )
                temploral_upload_record_bulk.append(tmp_upload_record)
                continue

            owner_key = '_'.join([ubigeo, str(owner_code)])
            owner_item = LandOwner.objects.filter(ubigeo=ubigeo, code=owner_code).first()
            document_type = record.get('tip_doc')
            document = record.get('doc_iden')
            owner_record = self.land_owner_map(upload_history, record)

            if owner_item:
                owner_record_status = 2
                owner_record.update({
                    'id': owner_item.id,
                })
            elif owner_key not in owner_records_unique:
                owner_records_unique.append(owner_key)

                if document_type is not None and document is not None:

                    owner_item_document = LandOwner.objects.filter(
                        ubigeo=ubigeo, document_type=document_type, dni=document
                    )

                    if owner_item_document.exists():
                        tmp_upload_record = self._make_tmp_upload_record(
                            upload_history, record,
                            status='ERROR',
                            error_code='NOT_INSERT[exists_owner_with_document]'
                        )
                        temploral_upload_record_bulk.append(tmp_upload_record)
                        continue

                owner_record_status = 1
            else:
                owner_record_status = 0

            if land_record_status == 0 and owner_record_status == 0:
                tmp_upload_record = self._make_tmp_upload_record(
                    upload_history, record,
                    status='ERROR',
                    error_code='DUPLICATE'
                )
                temploral_upload_record_bulk.append(tmp_upload_record)
            else:
                tmp_upload_record = self._make_tmp_upload_record(
                    upload_history, record,
                    land_record=land_record,
                    land_record_status=land_record_status,
                    owner_record=owner_record,
                    owner_record_status=owner_record_status,
                    error_code='OK'
                )
                temploral_upload_record_bulk.append(tmp_upload_record)

        TemploralUploadRecord.objects.bulk_create(temploral_upload_record_bulk)

    def land_mapper(self):
        return {
                # 'id': 'id_pred',
                'id_land_cartographic': 'id_pred',
                'cpm': 'cod_pre',
                'id_plot': 'id_lote',
                'sec_ejec': 'sec_ejec',
                'ubigeo_id': 'ubigeo',
                'cup': 'cod_cpu',
                'cod_sect': 'cod_sect',
                'cod_uu': 'cod_uu',
                'cod_mzn': 'cod_mzn',
                'cod_land': 'cod_lote',
                'cod_cuc': 'cod_cuc',
                'uu_type': 'tipo_uu',
                'habilitacion_name': 'nom_uu',
                'reference_name': 'nom_ref',
                'urban_mza': 'mzn_urb',
                'urban_lot_number': 'lot_urb',
                'cod_street': 'cod_via',
                'street_type_id': 'tip_via',
                'street_name': 'nom_via',
                'street_name_alt': 'nom_alt',
                'municipal_number': 'num_mun',
                'block': 'block',
                'indoor': 'interior',
                'floor': 'piso',
                'km': 'km',
                'landmark': 'referencia',
                'municipal_address': 'dir_mun',
                'urban_address': 'dir_urb',
                'assigned_address': 'dir_asig',
                'longitude': 'coord_x',
                'latitude': 'coord_y',
                'id_aranc': 'id_aranc',
                'land_area': 'area_terreno',
                'front_length': 'longitud_frente',
                'location_park': 'ubicacion_parque',
                'group_use_desc': 'grupo_uso_desc',
                'number_inhabitants': 'cantidad_habitantes',
                'classification_land_desc': 'clasificacion_predio_desc',
                'build_status_desc': 'estado_construccion_desc',
                'property_type': 'tipo_predio (urbano, rural)',
                'self_assessment_total': 'autoavaluo_total',
                'condominium': 'condominio',
                'deduction': 'deduccion',
                'self_assessment_affection': 'autoavaluo_afecto',
                'source_information': 'fuente',
                'resolution_type': 'tdoc_res',
                'resolution_document': 'ndoc_res'
                }

    def land_owner_map(self, upload_history, record):
        return {
            'ubigeo_id': record.get('ubigeo'),
            'code': record.get('cod_contr'),
            'document_type': record.get('tip_doc'),
            'dni': record.get('doc_iden'),
            'name': record.get('nombre'),
            'paternal_surname': record.get('ap_pat'),
            'maternal_surname': record.get('ap_mat'),
            'description_owner': record.get('contribuyente'),
            'tax_address': record.get('dir_fiscal'),
            'upload_history_id': upload_history.id
        }

    def loaded_temporal(self, upload_history):
        UploadHistory.objects.filter(id=upload_history.id, status='IN_PROGRESS_TMP')\
            .update(status='LOADED_TMP')

    def cancel_last_upload(self, upload_history):
        UploadHistory.objects.exclude(id=upload_history.id)\
            .filter(Q(ubigeo=upload_history.ubigeo) &
                    Q(Q(status='IN_PROGRESS_TMP') | Q(status='LOADED_TMP') | Q(status='IN_PROGRESS')))\
            .update(status='CANCEL')

        #  ToDo: Cancelar la tarea de dramatiq
