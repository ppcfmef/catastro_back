from rest_framework import serializers


class NsrtmLandOwnerSerializer(serializers.Serializer):
    document_type = serializers.CharField()
    document = serializers.CharField()
    nane = serializers.CharField(allow_null=True, allow_blank=True)
    paternal_surname = serializers.CharField(allow_null=True, allow_blank=True)
    maternal_surname = serializers.CharField(allow_null=True, allow_blank=True)
    business_name = serializers.CharField(allow_null=True, allow_blank=True)
