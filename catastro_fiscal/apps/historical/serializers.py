from rest_framework import serializers
from .models import HistoricalRecord
# from apps.users.serializers import UserSerializer
# from apps.lands.serializers import LandDetailSerializer, LandOwnerDetailSerializer


class HistoricalUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="pk")
    module = serializers.CharField()
    action = serializers.CharField(source="event")
    record_date = serializers.DateTimeField(source="creation_date", format='%d/%m/%Y %H:%M')


class HistoricalSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="registered_by__id")
    dni = serializers.CharField(source="registered_by__dni")
    full_name = serializers.SerializerMethodField()
    role = serializers.CharField(source="registered_by__role__name")
    actions = serializers.IntegerField(source="actions_total")

    class Meta:
        fields = ('id', 'dni', 'full_name', 'role', 'actions')

    def get_full_name(self, obj):
        return f'{obj.get("registered_by__first_name")} {obj.get("registered_by__last_name")}'


class HistoricalRecordSerializer(serializers.ModelSerializer):

    content_object = serializers.SerializerMethodField()

    class Meta:
        model = HistoricalRecord
        fields = (
            'id', 'registered_by', 'content_type', 'type_event', 'creation_date',
            'event', 'module', 'object_id', 'content_object'
        )

    def get_content_object(self, obj):
        data = list()
        try:
            _content_object = obj.get_content_object()
            model = type(_content_object).__name__
            data.append(dict(key="Model", value=type(_content_object).__name__))
            data.append(dict(key="ID", value=_content_object.pk))
            data.append(dict(key="Tabla", value=_content_object._meta.db_table))
            data.append(dict(key="Fecha", value=obj.creation_date.strftime("%d/%m/%Y %H:%M:%S")))
            if model == "User":
                data.append(dict(key="Usuario", value=_content_object.username))
                data.append(dict(key="Nombre y Apellidos", value=_content_object.get_full_name()))
                data.append(dict(key="E-mail", value=_content_object.email))
            if model == "LandOwner":
                data.append(
                    dict(
                        key="Nombres y Apellidos",
                        value=f'{_content_object.name or ""} {_content_object.paternal_surname or ""} {_content_object.maternal_surname or ""}'
                    )
                )
                data.append(dict(key="DNI", value=_content_object.dni))
                data.append(dict(key="E-mail", value=_content_object.email or ""))
            if model == "Land":
                owner = _content_object.owner
                data.append(dict(key="Contribuyente", value=f'{owner.name or ""} {owner.paternal_surname or ""} {owner.maternal_surname or ""}'))
                data.append(dict(key="Estatus", value=_content_object.get_status_display()))
                data.append(dict(key="Ubigeo", value=_content_object.ubigeo))
            return data
        except Exception as e:
            return None
