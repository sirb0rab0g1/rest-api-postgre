from rest_framework import serializers
from .models import (
    Information,
)

class InformationSerializer(serializers.ModelSerializer):
    info = serializers.ReadOnlyField()

    class Meta:
        model = Information
        fields = '__all__'