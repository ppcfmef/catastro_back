from rest_framework import serializers

from .models import GisCategory, GisCatalog, GisService


class GisCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GisCategory
        fields = '__all__'


class GisServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GisService
        fields = '__all__'


class GisCatalogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GisCatalog
        fields = '__all__'


class GisCatalogDetailSerializer(serializers.ModelSerializer):
    services = GisServiceSerializer(many=True)

    class Meta:
        model = GisCatalog
        fields = '__all__'


class GisCatalogCreateSerializer(serializers.ModelSerializer):
    services = GisServiceSerializer(many=True, required=False)

    class Meta:
        model = GisCatalog
        fields = '__all__'

    def create(self, validated_data):
        services = validated_data.pop('services', [])
        catalog = super(GisCatalogCreateSerializer, self).create(validated_data)
        if services:
            new_services = []
            for service in services:
                new_service = GisService(**service)
                new_service.catalog = catalog
                new_services.append(new_service)
            GisService.objects.bulk_create(new_services)
        return catalog
