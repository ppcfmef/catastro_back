from rest_framework import serializers


class HistoricalUserSerializer(serializers.Serializer):
    module = serializers.CharField()
    action = serializers.CharField(source="event")
    record_date = serializers.DateTimeField(source="creation_date")


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
