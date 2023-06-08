import dramatiq
from rest_framework.exceptions import ValidationError
from apps.lands.models import UploadHistory
from .services.rt_contribuyente_upload_temporal import RTContribuyenteUploadTemporalService
from .services.income_upload import RTContribuyenteUploadService


@dramatiq.actor(queue_name='incomes_upload_tenporal', max_retries=0)
def process_incomes_upload_tenporal(upload_history_id: int):
    upload_history = UploadHistory.objects.get(pk=upload_history_id)

    if upload_history.type_upload == 'RT_CONTRIBUYENTE':
        RTContribuyenteUploadTemporalService().execute(upload_history)
    else:
        raise ValidationError('No existe tipo de carga para procesar')


@dramatiq.actor(queue_name='incomes_upload', max_retries=1)
def process_incomes_upload(upload_history_id: int):
    upload_history = UploadHistory.objects.get(pk=upload_history_id)

    if upload_history.type_upload == 'RT_CONTRIBUYENTE':
        RTContribuyenteUploadService().execute(upload_history)
    else:
        raise ValidationError('No existe tipo de carga para procesar')
