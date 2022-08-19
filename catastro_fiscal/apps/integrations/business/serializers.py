from rest_framework import serializers


class BusinessIntegrationSerializer(serializers.Serializer):
    document = serializers.CharField()
    business_name = serializers.CharField()
