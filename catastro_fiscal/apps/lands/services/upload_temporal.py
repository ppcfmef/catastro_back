from ..models import UploadHistory, TemploralUploadRecord, Land, LandOwner
from .read_xlsx import ReadXlsxService


class UploadTemporalService:

    read_file_service = ReadXlsxService

    def execute(self, upload_history: UploadHistory):
        records = self.read(upload_history)
        self.temporal_upload(upload_history, records)
        self.cancel_last_upload(upload_history)

    def read(self, upload_history):
        return self.read_file_service(file=upload_history.file_upload.file).read()

    def update_ubigeo(self, upload_history, records):
        if len(records) > 0:
            record = records[0]
            upload_history.ubigeo_id = str(record.get('ubigeo')).strip()
            upload_history.save()

    def temporal_upload(self, upload_history, records):
        temploral_upload_record_bulk = []
        land_document_all = self.get_owner_documents_upload(records)
        land_owner_exist = list(LandOwner.objects.filter(dni__in=land_document_all).values_list('dni', flat=True))
        land_owner_news = list(set(land_document_all) - set(land_owner_exist))

        land_record_cpu = []
        land_record_cpm = []
        for record in records:
            # owner
            owner_record_status = 0
            owner_record = None
            document_type = record.get('tip_doc')
            if self.document_exists(document_type):
                document = self.make_document(record)
                owner_record = self.land_owner_map(upload_history, record)
                if document in land_owner_news:
                    owner_record_status = 1
                    land_owner_news.remove(document)
                elif document in land_owner_exist:
                    owner_record_status = 2
                else:
                    owner_record_status = 0

            # Land
            land_record_status = 0
            land_record = None
            error_record = None

            cpu = record.get('cod_cpu')
            ubigeo = record.get('ubigeo')
            cpm = record.get('cod_pre')

            error_code = None
            if (cpu is not None and cpu != "") or (cpm is not None and cpm != ""):
                land_mappers = self.land_mapper()
                land_record = {key: record.get(value) for key, value in land_mappers.items()}
                land_record.update({
                    'upload_history_id': upload_history.id,
                    'source': 'carga_masiva'
                })
                longitude = record.get('coord_x')
                latitude = record.get('coord_x')
                land_record.update({'status': int(longitude is not None and latitude is not None)})

                if cpu is not None and cpu != "":
                    land_item = Land.objects.filter(cup=cpu).first()
                    if land_item:
                        land_record_status = 2
                        land_record.update({
                            'id': land_item.id,
                        })
                    elif cpu not in land_record_cpu:
                        land_record_status = 1
                        land_record_cpu.append(cpu)
                    else:
                        land_record_status = 0
                        error_code = 'DUPLICATE'
                else:
                    ubigeo_cpm = '-'.join([ubigeo, cpm])
                    land_item = Land.objects.filter(ubigeo=ubigeo, cpm=cpm).first()
                    if land_item:
                        land_record_status = 2
                        land_record.update({
                            'id': land_item.id,
                        })
                    elif ubigeo_cpm not in land_record_cpm:
                        land_record_status = 1
                        land_record_cpm.append(ubigeo_cpm)
                    else:
                        land_record_status = 0
                        error_code = 'DUPLICATE'
            else:
                land_record_status = 0
                error_record = record
                error_code = 'IS_REQUIRED[cpu o cpm]'

            # actualizanod codigos de error
            status = 'ERROR'

            if land_record_status == 0:
                status = 'ERROR'
            elif land_record_status == 1:
                status = 'OK_NEW'
            elif land_record_status == 2:
                status = 'OK_OLD'

            tmp_upload_record = TemploralUploadRecord(
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
            temploral_upload_record_bulk.append(tmp_upload_record)

        TemploralUploadRecord.objects.bulk_create(temploral_upload_record_bulk)

    def land_mapper(self):
        return {
                # 'id': 'id_pred',
                'id_land_cartographic': 'id_pred',
                'cpm': 'cod_pre',
                'id_plot': 'id_lote',
                'sec_ejec': 'sec_ejec',
                'ubigeo': 'ubigeo',
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
                'street_type': 'tip_via',
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
        document = self.make_document(record)
        return {
            'code': record.get('cod_contr'),
            'document_type': record.get('tip_doc'),
            'dni': document,
            'name': record.get('nombre'),
            'paternal_surname': record.get('nombre'),
            'maternal_surname': record.get('ap_mat'),
            'description_owner': record.get('contribuyente'),
            'tax_address': record.get('dir_fiscal'),
            'upload_history_id': upload_history.id
        }

    def make_document(self, record):
        nonunique_document_types = ['00', '08']
        document_type = record.get('tip_doc')
        document = record.get('doc_iden')
        ubigeo = record.get('ubigeo')
        return '-'.join([ubigeo, document]) if document_type in nonunique_document_types else document

    def get_owner_documents_upload(self, records):
        """
        :param records: todos los registros leidos
        :return documents: Listado de numero de documentos unicos de los registros
        """
        land_document = []
        for record in records:
            document_type = record.get('tip_doc')
            if document_type is not None and str(document_type).strip() != "":
                land_document.append(self.make_document(record))
        return list(set(land_document))

    def document_exists(self, document_type):
        return document_type is not None and str(document_type).strip() != ''

    def get_temporal_summary(self, upload_history):
        temporal_records = TemploralUploadRecord.objects.filter(upload_history=upload_history)
        errors_data = temporal_records.filter(status='ERROR')
        corrects_data = temporal_records.filter(status__in=['OK_NEW', 'OK_OLD'])
        return {
            'upload_history_id': upload_history.id,
            'status': upload_history.status,
            'total': temporal_records.count(),
            'errors': errors_data.count(),
            'corrects': corrects_data.count(),
            'new': temporal_records.filter(status='OK_NEW').count(),
            'updates': temporal_records.filter(status='OK_OLD').count(),
            'errors_data': errors_data.values('record', 'error_code', 'status'),
            'corrects_data': corrects_data.values('record', 'status'),
        }

    def cancel_last_upload(self, upload_history):
        UploadHistory.objects.exclude(id=upload_history.id).filter(status="INITIAL", ubigeo=upload_history.ubigeo)\
            .update(status='CANCEL')
