from numpy import mean
from rest_framework import serializers
from .models import UserHappiness


class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHappiness
        fields = '__all__'