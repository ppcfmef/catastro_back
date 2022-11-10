from django.db.models import Q

from core.utils.exports import ExportView
from ..models import Land


class ExportRecordsView(ExportView):
    filename = 'records.xlsx'
    page_title = 'Listado de predios'
    headers = [
        'ID_PRED', 'COD_PRE', 'SEC_EJEC', 'UBIGEO', 'COD_CPU', 'COD_SECT', 'COD_UU', 'COD_MZN', 'COD_LOTE', 'COD_CUC',
        'TIPO_UU', 'NOM_UU', 'NOM_REF', 'MZN_URB', 'LOT_URB', 'COD_VIA', 'TIP_VIA', 'NOM_VIA', 'NOM_ALT', 'NUM_MUN',
        'BLOCK', 'INTERIOR', 'PISO', 'KM', 'REFERENCIA', 'DIR_MUN', 'DIR_URB', 'DIR_ASIG', 'COOR X', 'COOR Y',
        'ID_ARANC', 'TIP_DOC', 'DOC_IDEN', 'AP_PAT', 'AP_MAT', 'CONTRIBUYENTE',

    ]
    filters = ['ubigeo', 'status']

    def filter_queryset(self, queryset):
        queryset = super(ExportRecordsView, self).filter_queryset(queryset)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(cup__icontains=search) |
                Q(cpm__icontains=search) |
                Q(id_cartographic_img__icontains=search) |
                Q(id_plot__icontains=search) |
                Q(street_name__icontains=search)
            )
        return queryset

    def get_queryset(self):
        queryset = Land.objects.all().order_by('-creation_date')
        return self.filter_queryset(queryset)

    def get_content(self):
        queryset = self.get_queryset()
        content = []
        for land in queryset:
            content.append([
                land.id,
                land.cpm,
                land.sec_ejec,
                land.ubigeo,
                land.cup,
                land.cod_sect,
                land.cod_uu,
                land.cod_mzn,
                land.cod_land,
                land.cod_cuc,
                land.uu_type,
                land.habilitacion_name,
                land.reference_name,
                land.urban_mza,
                land.urban_lot_number,
                land.cod_street,
                land.street_type,
                land.street_name,
                land.street_name_alt,
                land.municipal_number,
                land.block,
                land.indoor,
                land.floor,
                land.km,
                land.landmark,
                land.municipal_address,
                land.urban_address,
                land.assigned_address,
                land.longitude,
                land.latitude,
                land.id_aranc,
                land.owner.document_type if land.owner else '',
                land.owner.dni if land.owner else '',
                land.owner.paternal_surname if land.owner else '',
                land.owner.maternal_surname if land.owner else '',
                land.owner.description_owner if land.owner else '',
            ])
        return content
