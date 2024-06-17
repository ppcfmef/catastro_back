import pandas as pd
from simpledbf import Dbf5
from django.conf import settings
from apps.lands.models import Land, LandOwner, LandOwnerDetail, UploadHistory


def land_map():
    return {

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

        'uu_type': 'tipo_uu',
        'habilitacion_name': 'nom_uu',
        'reference_name': 'nom_ref',
        'urban_mza': 'mzn_urb',
        'urban_lot_number': 'lot_urb',
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
        'land_area': 'area_terre',
        'front_length': 'longitud_f',
        'group_use_desc': 'grupo_uso_',
        'number_inhabitants': 'cantidad_h',
        'classification_land_desc': 'clasificac',
        'build_status_desc': 'estado_con',
        'property_type': 'tipo_predi',
        'self_assessment_total': 'autoavaluo',
        'condominium': 'condominio',
        'deduction': 'deduccion',
        'self_assessment_affection': 'autoaval_1',
        'source_information': 'fuente',
        'resolution_type': 'tdoc_res',
        'resolution_document': 'ndoc_res',

        'built_area': 'area_const',
        'id_cartographic_img': 'id_img',
        'apartment_number': 'num_dep'
    }


def land_owner():
    return {
        'ubigeo_id': 'ubigeo',
        'code': 'cod_contr',
        'document_type': 'tip_doc',
        'dni': 'doc_iden',
        'name': 'nombre',
        'paternal_surname': 'ap_pat',
        'maternal_surname': 'ap_mat',
        'description_owner': 'contribuye',
        #'tax_address': 'dir_fiscal'
    }


def run():
    dbf = Dbf5(settings.MEDIA_ROOT / 'tb_predio_lince.dbf')
    df = dbf.to_dataframe()

    map_land = land_map()
    map_owner = land_owner()
    map_land.update(map_owner)

    land_mapper = land_map()
    owner_mapper = land_owner()

    df.columns = df.columns.str.lower()
    df_land = df[list(map_land.values())]
    ubigeo = str(df_land.iloc[0]['ubigeo']).strip()[:6]
    records = df_land.where(pd.notnull(df_land), None).to_dict('records')
    land_key_unique = []
    land_records_unique = []
    owner_key_unique = []
    owner_records_unique = []

    upload_history = UploadHistory.objects.create(username="upload_initial", ubigeo_id=ubigeo)

    valid_records = []
    # Insertar masiva table de registros unicos
    for record in records:
        ubigeo_record = record.get('ubigeo')
        cpm = record.get('cod_pre')
        owner_code = record.get('cod_contr')

        if ubigeo_record is None:
            #print('>>> error ubigeo: ', record)
            continue

        if cpm is None:
            #print('>>> error cpm: ', record)
            continue

        if owner_code is None:
            #print('>>> error owner_code: ', owner_code)
            continue

        valid_records.append(record)
        owner_key = '_'.join([ubigeo, str(owner_code)])
        land_key = '_'.join([ubigeo, cpm])

        if owner_key not in owner_key_unique:
            owner_key_unique.append(owner_key)
            owner_record = {key: None if pd.isna(record.get(value)) else record.get(value)
                            for key, value in owner_mapper.items()}
            owner_record.update({'upload_history_id': upload_history.id})
            owner_records_unique.append(LandOwner(**owner_record))

        if land_key not in land_key_unique:
            land_key_unique.append(land_key)
            land_record = {key: None if pd.isna(record.get(value)) else record.get(value)
                           for key, value in land_mapper.items()}

            longitude = land_record.get('longitude')
            latitude = land_record.get('latitude')

            land_record.update({
                'longitude':  longitude if longitude else None,
                'latitude': latitude if longitude else None,
                'upload_history_id': upload_history.id,
                'source': 'carga_masiva',
                'status': int(1 if longitude and latitude else 0)
            })
            land_records_unique.append(Land(**land_record))

        # print(ubigeo, cpm, owner_code)

    LandOwner.objects.bulk_create(owner_records_unique)
    Land.objects.bulk_create(land_records_unique)

    # Insertar tabla intermedia
    land_owner_details = []
    for record in valid_records:
        cpm = record.get('cod_pre')
        owner_code = record.get('cod_contr')

        land = Land.objects.get(ubigeo_id=ubigeo, cpm=cpm)
        owner = LandOwner.objects.get(ubigeo_id=ubigeo, code=owner_code)
        land_owner_details.append(LandOwnerDetail(land=land, owner=owner, ubigeo_id=ubigeo))

    LandOwnerDetail.objects.bulk_create(land_owner_details)

    # contador de predios
    for landowner in upload_history.landowner_set.all():
        number_lands = LandOwnerDetail.objects.filter(owner_id=landowner.id).count()
        LandOwner.objects.filter(id=landowner.id).update(number_lands=number_lands)
