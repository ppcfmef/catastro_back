from datetime import datetime

from core.utils.exports import ExportView
from apps.lands.models import TemploralUploadRecord


class TemporalUploadRecordExportView(ExportView):
    page_title = 'Historial de carga'
    headers = [
        'STATUS', 'ERROR_CODE',
        'OBJECTID', 'ID_PRED', 'COD_PRE', 'SEC_EJEC', 'UBIGEO', 'ID_LOTE', 'COD_CPU', 'COD_SECT', 'COD_UU', 'COD_MZN',
        'COD_LOTE', 'TIPO_UU', 'NOM_UU', 'NOM_REF', 'MZN_URB', 'LOT_URB', 'TIP_VIA', 'NOM_VIA', 'NOM_ALT', 'NUM_MUN',
        'NUM_ALT', 'BLOCK', 'NUM_DEP', 'INTERIOR', 'PISO', 'KM', 'REFERENCIA', 'DIR_MUN', 'DIR_URB', 'DIR_ASIG',
        'COORD_X', 'COORD_Y', 'ID_ARANC', 'TIP_DOC', 'DOC_IDEN', 'COD_CONTR', 'NOMBRE', 'AP_PAT', 'AP_MAT',
        'CONTRIBUYENTE', 'DIR_FISCAL', 'ESTADO', 'Area_terreno', 'Area_construida', 'Longitud_frente', 'DIS_PAR',
        'Grupo_uso_desc', 'Cantidad_habitantes', 'Clasificacion_predio_desc', 'Estado_construccion_desc',
        'Tipo_predio', 'Autoavaluo_total', 'Condominio', 'Deduccion', 'Autoavaluo_afecto', 'FUENTE', 'TDOC_RES',
        'NDOC_RES', 'L_FOTO', 'ID_IMG', 'ESTADO_P', 'VAL_ACT', 'RAN_CPU', 'COD_UI', 'COD_VER',
    ]

    def filter_queryset(self, queryset):
        queryset = super(TemporalUploadRecordExportView, self).filter_queryset(queryset)
        upload_history = self.kwargs.get('upload_history', None)
        if upload_history:
            queryset = queryset.filter(upload_history_id=upload_history)
        status_choices = {
            'OK': ['OK_NEW', 'OK_OLD'],
            'ERROR': ['ERROR']
        }
        status = self.request.GET.get('status')
        if status and status in status_choices:
            queryset = queryset.filter(status__in=status_choices[status])
        return queryset

    def get_queryset(self):
        queryset = TemploralUploadRecord.objects.all().order_by('id')
        return self.filter_queryset(queryset)

    def get_content(self):
        queryset = self.get_queryset()
        content = []
        for record in queryset:
            data = record.record
            content.append([
                record.status,
                record.error_code,
                data.get('objectid', ''),
                data.get('id_pred', ''),
                data.get('cod_pre', ''),
                data.get('sec_ejec', ''),
                data.get('ubigeo', ''),
                data.get('id_lote', ''),
                data.get('cod_cpu', ''),
                data.get('cod_sect', ''),
                data.get('cod_uu', ''),
                data.get('cod_mzn', ''),
                data.get('cod_lote', ''),
                data.get('tipo_uu', ''),
                data.get('nom_uu', ''),
                data.get('nom_ref', ''),
                data.get('mzn_urb', ''),
                data.get('lot_urb', ''),
                data.get('tip_via', ''),
                data.get('nom_via', ''),
                data.get('nom_alt', ''),
                data.get('num_mun', ''),
                data.get('num_alt', ''),
                data.get('block', ''),
                data.get('num_dep', ''),
                data.get('interior', ''),
                data.get('piso', ''),
                data.get('km', ''),
                data.get('referencia', ''),
                data.get('dir_mun', ''),
                data.get('dir_urb', ''),
                data.get('dir_asig', ''),
                data.get('coord_x', ''),
                data.get('coord_y', ''),
                data.get('id_aranc', ''),
                data.get('tip_doc', ''),
                data.get('doc_iden', ''),
                data.get('cod_contr', ''),
                data.get('nombre', ''),
                data.get('ap_pat', ''),
                data.get('ap_mat', ''),
                data.get('contribuyente', ''),
                data.get('dir_fiscal', ''),
                data.get('estado', ''),
                data.get('area_terreno', ''),
                data.get('area_construida', ''),
                data.get('longitud_frente', ''),
                data.get('dis_par', ''),
                data.get('grupo_uso_desc', ''),
                data.get('cantidad_habitantes', ''),
                data.get('clasificacion_predio_desc', ''),
                data.get('estado_construccion_desc', ''),
                data.get('tipo_predio', ''),
                data.get('autoavaluo_total', ''),
                data.get('condominio', ''),
                data.get('deduccion', ''),
                data.get('autoavaluo_afecto', ''),
                data.get('fuente', ''),
                data.get('tdoc_res', ''),
                data.get('ndoc_res', ''),
                data.get('l_foto', ''),
                data.get('id_img', ''),
                data.get('estado_p', ''),
                data.get('val_act', ''),
                data.get('ran_cpu', ''),
                data.get('cod_ui', ''),
                data.get('cod_ver', ''),
            ])
        return content

    def get_filename(self):
        return f'historial_carga_{datetime.now().strftime("%m%d%Y%H%M%S")}.xlsx'
