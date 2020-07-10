from rest_framework import serializers
from . import models
from rest_framework.validators import UniqueValidator


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consumer
        read_only_fields    =   ['id', 'delete_status']
        write_only_fields   =   ['password']
        fields              =   ('id', 'first_name', 'last_name', 'address', 'pincode', 'email', 'password', 'phone', 'delete_status' )

        extra_kwargs = {
            'email': {'validators': [UniqueValidator(queryset=model.objects.all())]},
            'phone': {'validators': [UniqueValidator(queryset=model.objects.all())]},
        }

def __init__(self):
    return self.title
