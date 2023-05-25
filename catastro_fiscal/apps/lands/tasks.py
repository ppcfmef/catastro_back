import dramatiq
from .models import UploadHistory
from .services.upload_temporal import UploadTemporalService


@dramatiq.actor
def process_upload_tenporal(upload_history_id: int):
    upload_history = UploadHistory.objects.get(pk=upload_history_id)
    UploadTemporalService().execute(upload_history)
