from rest_framework import serializers
from .models import Navigation


class NavigationSerializer(serializers.ModelSerializer):
    full_title = serializers.CharField(read_only=True)

    class Meta:
        model = Navigation
        fields = '__all__'


class NavigationTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Navigation
        fields = ('id', 'title', 'subtitle', 'type', 'icon', 'link', 'order')

    def to_representation(self, obj):
        if 'children' in obj:
            self.fields['children'] = NavigationTreeSerializer(obj, many=True)
        return super(NavigationTreeSerializer, self).to_representation(obj)
