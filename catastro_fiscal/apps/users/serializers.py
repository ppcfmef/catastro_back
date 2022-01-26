from rest_framework import serializers
from .models import User


class UserProfileShortSerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'name', 'email')
