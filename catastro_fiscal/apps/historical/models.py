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
        instance.module = instance.get_module(obj, module)
        instance.event = instance.get_event(obj, event)
        instance.save()

    def get_event(self, obj, event):
        _event = event or ""
        subjects = {
            "User": "usuario",
            "LandOwner": "contribuyente",
            "Land": "punto lote",
        }
        subject = subjects.get(type(obj).__name__)
        if not event:
            _event = f'{self.type_event.label} de un {subject} con ID: {obj.pk}'
        return _event

    def get_module(self, obj, module=None):
        _module = module or ""
        modules = {
            "User": "Gestor de Usuarios - Usuarios",
            "LandOwner": "Gestor de predios - Registro de Contribuyentes y Predios",
            "Land": "Gestor de predios - Registro de Contribuyentes y Predios",
        }
        if not module:
            _module = modules.get(type(obj).__name__)
        return _module

    def get_content_object(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)