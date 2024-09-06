import pandas as pd
from simpledbf import Dbf5
from django.conf import settings
from apps.lands.models import Land, LandOwner, LandOwnerDetail, UploadHistory
from os import path


def land_map():
    return {
        'id_lote_puerta' : 'id_lote_sirv',
        'id_lote_p':'ID_LOTE_P',
        'ubigeo_id': 'UBIGEO',
        'cpm': 'COD_PRE',
        'cup': 'COD_CPU',
        'resolution_document':'PARTIDA',
        'id_land_cartographic': 'ID_PRE',
        'sec_ejec': 'SEC_EJEC',
        'id_plot': 'ID_LOTE',
        'cod_sect': 'COD_SECT',
        'cod_mzn': 'COD_MZN',
        'cod_uu': 'COD_UU',
        'cod_land': 'COD_LOTE',
        'uu_type': 'TIPO_UU',
        'habilitacion_name': 'NOM_UU',
        'reference_name': 'NOM_REF',
        'urban_mza': 'MZN_URB',
        'urban_lot_number': 'LOT_URB',
        'street_type_id': 'TIP_VIA',
        'street_name': 'NOM_VIA',
        'street_name_alt': 'NOM_ALT',
        'municipal_number': 'NUM_MUN',
        'block': 'BLOCK',
        'indoor': 'INTERIOR',
        'floor': 'PISO',
        'km': 'KM',
        'landmark': 'REFERENCIA',
        'municipal_address': 'DIR_MUN',
        'urban_address': 'DIR_URB',
        'longitude': 'COORD_X',
        'latitude': 'COORD_Y',
        'id_aranc': 'ID_ARANC',
        'land_area': 'Area_terreno',
       
       # 'front_length': 'L_FRENTE',
         
    }






def run():
    excel_file = path.join(settings.MEDIA_ROOT , 'predio.xls')

    df = pd.read_excel(excel_file, dtype={'UBIGEO':str,'COD_SECT': str,'COD_MZN':str,'COD_UU':str,'COD_LOTE':str,'TIPO_UU':str,'TIP_VIA':str,'SEC_EJEC':str})

    queryset = Land.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).values('id','ubigeo_id','cup')
    df_django = pd.DataFrame(list(queryset))

    land_mapper = land_map()
    batch_size =100
    land_records_unique =[]


    if len(queryset)>0:
        df_merged = pd.merge(df, df_django, how='left',left_on=['UBIGEO','COD_CPU'] ,right_on=['ubigeo_id','cup'] , indicator=True)
        # Filtrar los registros que no tienen correspondencia en el DataFrame derecho
        df_only_left = df_merged[df_merged['_merge'] == 'left_only']

        # Eliminar la columna '_merge'
        df_only_left = df_only_left.drop(columns=['_merge']+df_django.columns.to_list())

      
    else:
        df_only_left = df


    #print(df_only_left.columns.tolist())


    
    for index, record in df_only_left.iterrows():
        
        land_record = {key: None if pd.isna(record.get(value)) else record.get(value)
                           for key, value in land_mapper.items()}
        land_record['street_type_id'] = None if  land_record['street_type_id']=='-' else land_record['street_type_id']
        
        land_record['resolution_type'] = '1' if record['PARTIDA'] else None 

        longitude = land_record.get('longitude')
        latitude = land_record.get('latitude')
        land_record.update({
                
                'source': 'registro_predios' if record['NOM_PC'] == 'PLATAFORMA' else 'mantenimiento_carto' if  record['NOM_PC'] == 'PCF' else 'carga_masiva' ,
                'status': int(1 if longitude and latitude else 0),
                'cod_tipo_predio_id':1
            })
        
        land_records_unique.append(Land(**land_record))

        if len(land_records_unique) == batch_size : 
            Land.objects.bulk_create(land_records_unique)
            land_records_unique = []
            
    Land.objects.bulk_create(land_records_unique)



# def contribuyente_map():
#     return {
#         'UBIGEO': 'ubigeo',
#         'CODIGO_CONTRIBUYENTE':	'cod_contr',
#         'CODIGO_TIPO_DE_CONTRIBUYENTE':	'tipo_contribuyente_id',
#         'CODIGO_TIPO_DOCUMENTO_DE_IDENTIDAD': 'tip_doc',
#         'NUM_DOC_IDENTIDAD': 'doc_iden',
#         'NOMBRES': 'nombre',
#         'APELLIDO_PATERNO':	'ap_pat',
#         'APELLIDO_MATERNO':	'ap_mat',
#         'RAZON_SOCIAL':	'contribuyente',
#         'CORREO':	'correo_electronico',
#         'TELEFONO':	'telefono',


#     }


# def domicilio_map():
#     return  {
#     'UBIGEO': 'ubigeo',
#     'CODIGO_CONTRIBUYENTE':	'cod_contr',
#     'CODIGO_TIPO_DE_CONTRIBUYENTE':	'tipo_contribuyente_id',
#     'CODIGO_TIPO_DOCUMENTO_DE_IDENTIDAD': 'tip_doc',
#     'NUM_DOC_IDENTIDAD': 'doc_iden',
#     'NOMBRES': 'nombre',
#     'APELLIDO_PATERNO':	'ap_pat',
#     'APELLIDO_MATERNO':	'ap_mat',
#     'RAZON_SOCIAL':	'contribuyente',
#     'CORREO':	'correo_electronico',
#     'TELEFONO':	'telefono',
# }