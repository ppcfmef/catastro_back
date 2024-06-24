import pandas as pd
from simpledbf import Dbf5
from django.conf import settings
from apps.lands.models import Land, LandOwner, LandOwnerDetail, UploadHistory, Domicilio
from os import path


<<<<<<< HEAD
def predio_contribuyente_predio_map():
    return {
   
=======
def predio_contribuyente_map():
    return {
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43
        'cup': 'COD_CPU' ,
        'cpm': 'COD_CPM' ,
        'code':'COD_CONTRIBUYENTE',
        'ubigeo_id':'UBIGEO',
        'land_id':'land_id',
        'owner_id':'owner_id',
        'area_terreno':'AREA_TERRENO',
     
        'area_construida':'AREA_CONSTRUIDA',
        'area_tot_terr_comun':'AREA_TOT_TERR_COMUN',
        'area_tot_cons_comun':'AREA_TOT_CONS_COMUN',
        'por_propiedad':'POR_PROPIEDAD',
        'tip_transferencia_id':'TIP_TRANSFERENCIA_ID',
<<<<<<< HEAD
        'tip_uso_predio_id':'TIP_USO_PREDIO_ID',
        'tip_propiedad_id':'TIP_PROPIEDAD_ID',
        'fec_transferencia':'FECHA_TRANSFERENCIA',
=======
         'tip_uso_predio_id':'TIP_USO_PREDIO_ID',
          'tip_propiedad_id':'TIP_PROPIEDAD_ID',
          'fec_transferencia':'FECHA_TRANSFERENCIA',
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43
        'longitud_frente':'LONGITUD_FRENTE',
        'cantidad_habitantes':'CANTIDAD_HABITANTES',
        'pre_inhabitable':'PRE_INHABITABLE',
        'par_registral':'PAR_REGISTRAL',
        'numero_dj':'NUMERO_DJ',
<<<<<<< HEAD
        'fecha_dj':'FECHA_DJ',
        'usuario_creacion':'USUARIO_REGISTRADOR',
        'fecha_adquisicion':'FECHA_ADQUISICION',
        'anio_determinacion':'ANIO_DETERMINACION',

=======
    'fecha_dj':'FECHA_DJ',
    'usuario_creacion':'USUARIO_REGISTRADOR',
    #'anio':'ANIO_DETERMINACION',
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43
    
    }





def run():
  
    excel_file = path.join(settings.MEDIA_ROOT , 'contribuyente_predio.xlsx')

    df = pd.read_excel(excel_file, dtype={'UBIGEO':str ,'COD_CONTRIBUYENTE':str})

    df['FECHA_TRANSFERENCIA'] = pd.to_datetime(df['FECHA_TRANSFERENCIA'])
    df['FECHA_DJ'] = pd.to_datetime(df['FECHA_DJ'])
<<<<<<< HEAD
    df['FECHA_ADQUISICION'] =pd.to_datetime(df['FECHA_ADQUISICION'])
=======
    
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43
    queryset_land_owner = LandOwnerDetail.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).values('id','cup','ubigeo_id','code')

    queryset_land = Land.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).values('id','cup','ubigeo_id')
    queryset_owner = LandOwner.objects.filter(ubigeo__in=['040403', '040502', '040509', '040510', '040513', '040604', '040607', '040811', '150401', '061005', '250201', '100704', '110404', '021510']).values('id','code','ubigeo_id')
    

    
    df_django_land = pd.DataFrame(list(queryset_land))
    df_django_owner = pd.DataFrame(list(queryset_owner))
    df_django_land_owner = pd.DataFrame(list(queryset_land_owner))
<<<<<<< HEAD
    predio_cont_map = predio_contribuyente_predio_map()
=======
    predio_cont_map = predio_contribuyente_map()
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43

    batch_size =100

    if len(df_django_land_owner)>0:
<<<<<<< HEAD
        print('df_django_land_owner',df_django_land_owner)
        df_merged_diff =  pd.merge(df, df_django_land_owner, how='left',left_on=['UBIGEO','COD_CONTRIBUYENTE','COD_CPU'] ,right_on=['ubigeo_id','code','cup'] , indicator=True)
=======
        df_merged_diff =  pd.merge(df, df_django_land_owner, how='left',left_on=['UBIGEO','CODIGO_CONTRIBUYENTE','COD_CPU'] ,right_on=['ubigeo_id','code','cup'] , indicator=True)
>>>>>>> 31fff1833d6d80d6c83a8bbe1535f32e50298d43
        df_merged_diff = df_merged_diff[df_merged_diff['_merge'] == 'left_only']

            # Eliminar la columna '_merge'
        df_merged_diff = df_merged_diff.drop(columns=['_merge']+df_django_land_owner.columns.to_list())
        df =df_merged_diff

    

    df_merged = pd.merge(df, df_django_land,left_on=['UBIGEO','COD_CPU'] ,right_on=['ubigeo_id','cup'] , indicator=True)
 
    df_merged = df_merged.drop(columns=['_merge','ubigeo_id','cup'])    

    df_merged = df_merged.rename(columns={'id':'land_id'})


    df_merged = pd.merge(df_merged, df_django_owner,left_on=['UBIGEO','COD_CONTRIBUYENTE'] ,right_on=['ubigeo_id','code'] , indicator=True)
    df_merged = df_merged.drop(columns=['_merge','ubigeo_id','code'])    

    df_merged = df_merged.rename(columns={'id':'owner_id'})

    
    print(df_merged)


    records_unique =[]
    for index, record in df_merged.iterrows():
        
        
        record_unique = {key: None if pd.isna(record.get(value)) else record.get(value)
                           for key, value in predio_cont_map.items()}
        
        

        record_unique['estado']= 1 if record['ESTADO_REGISTRO'] =='ACTIVO' else 0 
        #print('record_unique>>',record_unique)
        records_unique.append( LandOwnerDetail(**record_unique))


        

        if len(records_unique) == batch_size : 
            print('records_unique>>',records_unique)
            
            LandOwnerDetail.objects.bulk_create(records_unique)
            records_unique = []
            
    LandOwnerDetail.objects.bulk_create(records_unique)

    