from rest_framework import serializers
from .models import (
    Information,
)
from rest_framework.validators import UniqueValidator


class InformationSerializer(serializers.ModelSerializer):
    info = serializers.ReadOnlyField()

    class Meta:
        model = Information
        extra_kwargs = {
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=Information.objects.all(),
                        message='True')
                ],
            },
            'first_name': {
                'validators': [
                    UniqueValidator(
                        queryset=Information.objects.all(),
                        message='True')
                ],
            }
        }

        fields = '__all__'
