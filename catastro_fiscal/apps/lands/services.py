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

        land_document_all = self.get_owner_documents_upload(records)
        land_owner_exist = list(LandOwner.objects.filter(dni__in=land_document_all).values_list('dni', flat=True))
        land_owner_news = list(set(land_document_all) - set(land_owner_exist))

        for record in records:
            # owner
            owner_record_status = 0
            owner_record = None
            document_type = record.get('tip_doc')
            if document_type is not None and str(document_type).strip() != "":
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

            land_record_cpu = []
            land_record_cpm = []
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
                #'document_type': 'tip_doc',
                #'document': 'doc_iden',
                #'cod_owner': 'cod_contr',
                #'name': 'nombre',
                #'paternal_surname': 'ap_pat',
                #'maternal_surname': 'ap_mat',
                #'description_owner': 'contribuyente',
                #'phone': '',
                #'email': '',
                #'tax_address': 'dir_fiscal',
                #'status': 'estado',
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
    def land_owner_upload(self, upload_history):
        # Insertar nuevos
        temploral_records = TemploralUploadRecord.objects.filter(upload_history=upload_history, owner_record_status=1)
        land_owners_bulk = []
        for temploral in temploral_records:
            land_owners_bulk.append(LandOwner(**temploral.owner_record))
        LandOwner.objects.bulk_create(land_owners_bulk)

        # actualizacion diferencial

    def count_lands_by_owner(self):
        lands = Land.objects.values('owner').annotate(number_lands=Count('owner'))
        for land in lands:
            LandOwner.objects.filter(id=land['owner']).update(number_lands=land['number_lands'])

    def execute(self, upload_history: UploadHistory):
        records = self.read(upload_history)
        self.temporal_upload(upload_history, records)
        self.land_owner_upload(upload_history)
        self.land_upload(upload_history)
        self.count_lands_by_owner()

    def make_document(self, record):
        document_type = record.get('tip_doc')
        document = record.get('doc_iden')
        ubigeo = record.get('ubigeo')
        return '-'.join([ubigeo, document]) if document_type in ['00', '08'] else document

    def get_documents_upload(self, temploral_records):
        land_document = []
        for temploral in temploral_records:
            record = temploral.record
            document_type = record.get('tip_doc')
            if document_type is not None and str(document_type).strip() != "":
                land_document.append(self.make_document(record))
        return list(set(land_document))

    def get_owner_documents_upload(self, records):
        land_document = []
        for record in records:
            document_type = record.get('tip_doc')
            if document_type is not None and str(document_type).strip() != "":
                land_document.append(self.make_document(record))
        return list(set(land_document))

    def get_land_upload(self, temploral_records):
        land_cpu_all = []
        land_cpm_all = []
        for temploral in temploral_records:
            record = temploral.record
            cpu = record.get('cod_cpu')
            cpm = record.get('cod_pre')
            if cpu is not None and cpu != '':
                land_cpu_all.append(cpu)
            if (cpu is None or cpu == '') and (cpm is not None and cpm != ''):
                land_cpm_all.append(cpm)
        land_cpu_all = list(set(land_cpu_all))
        land_cpm_all = list(set(land_cpm_all))
