from rest_framework import serializers
from . import models
from consumer.serializer import ConsumerSerializer


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Request
        read_only_fields = ['id', 'status', 'request_time']
        fields = ('id', 'consumer', 'provider', 'description', 'status', 'request_time')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['consumer'] = ConsumerSerializer(instance.consumer).data
        return response

def __init__(self):
    return self.title
