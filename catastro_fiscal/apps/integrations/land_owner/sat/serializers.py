from rest_framework import serializers


class SattDataSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    appaterno = serializers.CharField()
    apmaterno = serializers.CharField()
    nrodocumento = serializers.CharField()


class SattValidateSerializer(serializers.Serializer):
    data = SattDataSerializer(many=True, allow_null=True, default=[])
    status = serializers.IntegerField()
    msj = serializers.CharField()
