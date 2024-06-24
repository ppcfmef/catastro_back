import pandas as pd
from simpledbf import Dbf5
from django.conf import settings
from apps.lands.models import Land, LandOwner, LandOwnerDetail, UploadHistory, Domicilio
from os import path


def contribuyente_map():
    return {
<<<<<<< HEAD
        'sec_ejec':'CODIGO_MUNICIPALIDAD',
    'ubigeo_id': 'UBIGEO_REGISTRO' ,
=======
    'ubigeo_id': 'UBIGEO' ,
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43
    'code': 'CODIGO_CONTRIBUYENTE'	,
    'tipo_contribuyente_id': 'CODIGO_TIPO_DE_CONTRIBUYENTE',
    'document_type_id':'CODIGO_TIPO_DOCUMENTO_IDENTIDAD' ,
    'dni':'NUM_DOC_IDENTIDAD' ,
    'name':'NOMBRES',
    'paternal_surname':'APELLIDO_PATERNO',
    'maternal_surname': 'APELLIDO_MATERNO',
    'description_owner':'RAZON_SOCIAL',
<<<<<<< HEAD
    # 'email':	'CORREO',
    # 'phone':	'TELEFONO',
=======
    'email':	'CORREO',
    'phone':	'TELEFONO',
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43


    }



def domicilio_map():

    return  {
        'contribuyente_id':'id',
        'ubigeo' : 'UBIGEO_DOM_FISCAL',
        'des_domicilio':'DESCRIPCION_DE_DOMICILIO_FISCAL',


    }  



def run():
    equivalencia_tipo_documento_identidad = {1: '01', 2: '06', 7: '00'}
    excel_file = path.join(settings.MEDIA_ROOT , 'contribuyente.xlsx')

    df = pd.read_excel(excel_file, dtype={'UBIGEO':str,'NUM_DOC_IDENTIDAD': str,'TELEFONO':str,'CODIGO_CONTRIBUYENTE':str})

    queryset = LandOwner.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).values()
    
    
    df_django = pd.DataFrame(list(queryset))
    print(df_django.columns.tolist())

    land_mapper = contribuyente_map()
    domicilio_mapper = domicilio_map()
    batch_size =100
    owner_records_unique =[]

    if len(queryset)>0:
        df_merged = pd.merge(df, df_django, how='left',left_on=['UBIGEO','CODIGO_CONTRIBUYENTE'] ,right_on=['ubigeo_id','code'] , indicator=True)
        # Filtrar los registros que no tienen correspondencia en el DataFrame derecho
        df_only_left = df_merged[df_merged['_merge'] == 'left_only']

        # Eliminar la columna '_merge'
        df_only_left = df_only_left.drop(columns=['_merge']+df_django.columns.to_list())

        #print(df_only_left.columns.tolist())
    else:
        df_only_left = df
    
    for index, record in df_only_left.iterrows():
        
        
        owner_record = {key: None if pd.isna(record.get(value)) else record.get(value)
                           for key, value in land_mapper.items()}
        
        owner_record['tipo_contribuyente_id'] =1 if record['TIPO_DE_CONTRIBUYENTE'] =='PERSONA NATURAL' else 2 if record['TIPO_DE_CONTRIBUYENTE'] =='PERSONA JURIDICA' else 3
        owner_record['name'] = record['RAZON_SOCIAL']   if owner_record['tipo_contribuyente_id'] == 3 else  owner_record['name']
            
        if owner_record['document_type_id'] is not None:
            owner_record['document_type_id'] =equivalencia_tipo_documento_identidad.get(owner_record['document_type_id'],None)

        
        owner_records_unique.append( LandOwner(**owner_record))




        if len(owner_records_unique) == batch_size : 
            print('owner_records_unique>>',owner_records_unique)
            LandOwner.objects.bulk_create(owner_records_unique)
            owner_records_unique = []
            
    LandOwner.objects.bulk_create(owner_records_unique)
<<<<<<< HEAD
    
    #Domicilio.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).values('id','ubigeo_id','code')
    
=======

>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43
    queryset_domicilios = LandOwner.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).values('id','ubigeo_id','code')
    
    df_django_domicilios = pd.DataFrame(list(queryset_domicilios))
    
    df_merged_cont_domicilio = pd.merge(df, df_django_domicilios,left_on=['UBIGEO','CODIGO_CONTRIBUYENTE'] ,right_on=['ubigeo_id','code'] , indicator=True)
<<<<<<< HEAD
    
=======
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43
    
    df_merged_contribuyente_domicilio = df_merged_cont_domicilio.drop(columns=['_merge']+['ubigeo_id','code'])
    

    domicilio_records= []
    
    domicilios  = Domicilio.objects.filter(contribuyente_id = list(queryset_domicilios.values_list(id,flat=True)))
    domicilios.delete()

    
    for index, record in df_merged_contribuyente_domicilio.iterrows():
        domicilio_record = {key: None if pd.isna(record.get(value)) else record.get(value)
                           for key, value in domicilio_mapper.items()}
        
        domicilio_record['contribuyente_id']= record['id']
        domicilio_records.append(Domicilio(**domicilio_record))

        
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