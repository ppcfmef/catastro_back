from apps.lands.views import UploadHistoryViewset
from .serializers import IncomeUploadHistorySerializer


class IncomeUploadHistoryViewset(UploadHistoryViewset):
    create_serializer_class = IncomeUploadHistorySerializer
