from rest_framework import serializers
from . import models
from rest_framework.validators import UniqueValidator


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        read_only_fields    =   ['id', 'delete_status']
        write_only_fields   =   ['password']
        fields              =   ('id', 'first_name', 'last_name', 'address', 'pincode', 'email', 'password', 'phone', 'service_type', 'base_price', 'rate_per_km', 'delete_status' )

        extra_kwargs = {
            'email': {'validators': [UniqueValidator(queryset=model.objects.all())]},
            'phone': {'validators': [UniqueValidator(queryset=model.objects.all())]},
        }
