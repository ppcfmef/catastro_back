import dramatiq
from .models import UploadHistory
from .services.upload_temporal import UploadTemporalService
from .services.upload_land import UploadLandService


@dramatiq.actor(queue_name='upload_tenporal', max_retries=0)
def process_upload_tenporal(upload_history_id: int):
    upload_history = UploadHistory.objects.get(pk=upload_history_id)
    UploadTemporalService().execute(upload_history)


@dramatiq.actor(queue_name='upload_land', max_retries=1)
def process_upload_land(upload_history_id: int):
    upload_history = UploadHistory.objects.get(pk=upload_history_id)
    UploadLandService().execute(upload_history)
