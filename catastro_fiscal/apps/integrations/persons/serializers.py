from rest_framework import serializers


class PersonIntegrationSerializer(serializers.Serializer):
    document = serializers.CharField()
    nane = serializers.CharField()
    paternal_surname = serializers.CharField()
    maternal_surname = serializers.CharField()
