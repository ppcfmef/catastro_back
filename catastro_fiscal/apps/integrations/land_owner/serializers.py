from rest_framework import serializers


class IntegrationResponseSerializer(serializers.Serializer):
    document = serializers.CharField()
    document_type = serializers.CharField()
    nane = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    paternal_surname = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    maternal_surname = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    business_name = serializers.CharField(allow_null=True, allow_blank=True, default=None)
