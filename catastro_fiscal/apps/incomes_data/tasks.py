import dramatiq
from rest_framework.exceptions import ValidationError
from apps.lands.models import UploadHistory
from .services.rt_contribuyente_upload_temporal import RTContribuyenteUploadTemporalService
from .services.rt_marcopredio_upload_temporal import RTMarcoPredioUploadTemporalService
from .services.rt_arancel_upload_temporal import RTArancelUploadTemporalService
from .services.rt_prediodato_upload_temporal import RTPredioDatoUploadTemporalService
from .services.rt_prediocaracteristica_upload_temporal import RTPredioCaracteristicaUploadTemporalService
from .services.rt_recaudacion_temporal import RTRecaudacionUploadTemporalService
from .services.rt_deuda_temporal import RTDeudaUploadTemporalService
from .services.income_upload import (
    RTContribuyenteUploadService, RTMarcoPredioUploadService, RTArancelUploadService, RTPredioDatoUploadService,
    RTPredioCaracteristicaUploadService, RTRecaudacionUploadService, RTDeudaUploadService
)


@dramatiq.actor(queue_name='incomes_upload_tenporal', max_retries=0)
def process_incomes_upload_tenporal(upload_history_id: int):
    upload_history = UploadHistory.objects.get(pk=upload_history_id)

    if upload_history.type_upload == 'RT_CONTRIBUYENTE':
        RTContribuyenteUploadTemporalService().execute(upload_history)
    elif upload_history.type_upload == 'RT_MARCO_PREDIO':
        RTMarcoPredioUploadTemporalService().execute(upload_history)
    elif upload_history.type_upload == 'RT_ARANCEL':
        RTArancelUploadTemporalService().execute(upload_history)
    elif upload_history.type_upload == 'RT_PREDIO_DATO':
        RTPredioDatoUploadTemporalService().execute(upload_history)
    elif upload_history.type_upload == 'RT_PREDIO_CARACT':
        RTPredioCaracteristicaUploadTemporalService().execute(upload_history)
    elif upload_history.type_upload == 'RT_RECAUDACION':
        RTRecaudacionUploadTemporalService().execute(upload_history)
    elif upload_history.type_upload == 'RT_DEUDA':
        RTDeudaUploadTemporalService().execute(upload_history)
    else:
        raise ValidationError('No existe tipo de carga para procesar')


@dramatiq.actor(queue_name='incomes_upload', max_retries=1)
def process_incomes_upload(upload_history_id: int):
    upload_history = UploadHistory.objects.get(pk=upload_history_id)

    if upload_history.type_upload == 'RT_CONTRIBUYENTE':
        RTContribuyenteUploadService().execute(upload_history)
    elif upload_history.type_upload == 'RT_MARCO_PREDIO':
        RTMarcoPredioUploadService().execute(upload_history)
    elif upload_history.type_upload == 'RT_ARANCEL':
        RTArancelUploadService().execute(upload_history)
    elif upload_history.type_upload == 'RT_PREDIO_DATO':
        RTPredioDatoUploadService().execute(upload_history)
    elif upload_history.type_upload == 'RT_PREDIO_CARACT':
        RTPredioCaracteristicaUploadService().execute(upload_history)
    elif upload_history.type_upload == 'RT_RECAUDACION':
        RTRecaudacionUploadService().execute(upload_history)
    elif upload_history.type_upload == 'RT_DEUDA':
        RTDeudaUploadService().execute(upload_history)
    else:
        raise ValidationError('No existe tipo de carga para procesar')
