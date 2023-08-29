from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractAudit
from apps.places.models import District
from apps.lands.models import Land
from django.contrib.auth import get_user_model



User = get_user_model()

