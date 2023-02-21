from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from apps.lands.models import Land, LandOwner

User = get_user_model()


class HistoricalRecord(models.Model):

    class RecordEvent(models.IntegerChoices):
        CREATED = 0, 'Generación'
        UPDATED = 1, 'Actualización'
        DELETED = 2, 'Eliminación'

    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    type_event = models.PositiveIntegerField(choices=RecordEvent.choices, default=RecordEvent.CREATED)
    creation_date = models.DateTimeField(
        _('creation date'),
        auto_now_add=True,
        help_text=_('record creation date')
    )
    event = models.TextField(blank=True)
    module = models.TextField(blank=True)
    object_id = models.IntegerField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        return self.event

    @classmethod
    def register(cls, user, obj, type_event, event=None, module=None):
        instance = cls(registered_by=user, object_id=obj.pk, type_event=type_event)
        instance.content_type = ContentType.objects.get_for_model(obj.__class__)
        if obj.__class__ == User:
            model = "usuario(a)"
            instance.module = "Gestor de Usuarios - Usuarios"
        elif obj.__class__ == LandOwner:
            model = "propetario(a)"
            if type_event == HistoricalRecord.RecordEvent.CREATED or type_event == HistoricalRecord.RecordEvent.UPDATED:
                instance.module = "Gestor de predios - Registro de Contribuyentes y Predios"
        elif obj.__class__ == Land:
            model = "punto lote"
            if type_event == HistoricalRecord.RecordEvent.CREATED or type_event == HistoricalRecord.RecordEvent.UPDATED:
                instance.module = "Gestor de predios - Registro de Contribuyentes y Predios"
        if event:
            pass
        else:
            instance.event = f'{cls.RecordEvent(type_event).label} de un {model}'
            instance.module = module or ""
        instance.save()

    def get_content_object(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)