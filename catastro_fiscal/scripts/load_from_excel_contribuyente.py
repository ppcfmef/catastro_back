import pandas as pd
from simpledbf import Dbf5
from django.conf import settings
from apps.lands.models import Land, LandOwner, LandOwnerDetail, UploadHistory, Domicilio
from os import path


def contribuyente_map():
    return {
    'ubigeo': 'UBIGEO' ,
    'cod_contr': 'CODIGO_CONTRIBUYENTE'	,
    'tipo_contribuyente_id': 'CODIGO_TIPO_DE_CONTRIBUYENTE',
    'tip_doc':'CODIGO_TIPO_DOCUMENTO_DE_IDENTIDAD' ,
    'doc_iden':'NUM_DOC_IDENTIDAD' ,
    'nombre':'NOMBRES',
    'ap_pat':'APELLIDO_PATERNO',
    'ap_mat': 'APELLIDO_MATERNO',
    'contribuyente':'RAZON_SOCIAL',
    'CORREO':	'correo_electronico',
    'TELEFONO':	'telefono',


    }



def domicilio_map():

    return  {
        'owner_id':'id',
        'ubigeo' : 'UBIGEO_DOM_FISCAL',
        'des_domicilio':'DESCRIPCION_DE_DOMICILIO_FISCAL',


    }  



def run():
    equivalencia_tipo_documento_identidad = {1: '01', 2: '06', 7: '00'}
    excel_file = path.join(settings.MEDIA_ROOT , 'contribuyente.xlsx')

    df = pd.read_excel(excel_file, dtype={'UBIGEO':str,'NUM_DOC_IDENTIDAD': str,'TELEFONO':str})

    queryset = LandOwner.objects.filter(ubigeo='100704').values()
    df_django = pd.DataFrame(list(queryset))

    land_mapper = contribuyente_map()
    domicilio_mapper = domicilio_map()
    batch_size =100
    owner_records_unique =[]

    
    df_merged = pd.merge(df, df_django, how='left',left_on=['UBIGEO','CODIGO_CONTRIBUYENTE'] ,right_on=['ubigeo_id','cod_contr'] , indicator=True)
    # Filtrar los registros que no tienen correspondencia en el DataFrame derecho
    df_only_left = df_merged[df_merged['_merge'] == 'left_only']

    # Eliminar la columna '_merge'
    df_only_left = df_only_left.drop(columns=['_merge']+df_django.columns.to_list())

    print(df_only_left.columns.tolist())


    
    for index, record in df_only_left.iterrows():
        
        
        owner_record = {key: None if pd.isna(record.get(value)) else record.get(value)
                           for key, value in land_mapper.items()}
        
        
        if owner_record['tip_doc'] is not None:
            owner_record['tip_doc'] =equivalencia_tipo_documento_identidad.get(owner_record['tip_doc'],None)

        
        owner_records_unique.append(owner_record)




        if len(owner_records_unique) == batch_size : 
            LandOwner.objects.bulk_create(owner_records_unique)
            owner_records_unique = []
            
    LandOwner.objects.bulk_create(owner_records_unique)

    queryset_domicilios = LandOwner.objects.filter(ubigeo='100704').values('id','ubigeo_id','code')
    
    df_django_domicilios = pd.DataFrame(list(queryset_domicilios))
    
    df_merged_cont_domicilio = pd.merge(df, df_django_domicilios, how='join',left_on=['UBIGEO','CODIGO_CONTRIBUYENTE'] ,right_on=['ubigeo_id','code'] , indicator=True)
    
    df_merged_contribuyente_domicilio = df_merged_cont_domicilio.drop(columns=['_merge']+['ubigeo_id','code'])
    

    domicilio_records= []
    
    for index, record in df_merged_contribuyente_domicilio.iterrows():
        domicilio_record = {key: None if pd.isna(record.get(value)) else record.get(value)
                           for key, value in domicilio_mapper.items()}
        

        domicilio_records.append(domicilio_record)

        
        if len(domicilio_records) == batch_size : 
            Domicilio.objects.bulk_create(domicilio_records)
            domicilio_records = []

    Domicilio.objects.bulk_create(domicilio_records)
    domicilio_records = []

        

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