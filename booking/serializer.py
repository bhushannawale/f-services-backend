from rest_framework import serializers
from . import models
from consumer.serializer import ConsumerSerializer
from provider.serializer import ProviderSerializer


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ('id', 'consumer', 'provider', 'description', 'amount', 'booking_time')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['consumer'] = ConsumerSerializer(instance.consumer).data
        response['provider'] = ProviderSerializer(instance.provider).data
        return response


class ErrorSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=20)
    Error = serializers.CharField(max_length=254)

    def __init__(self, Name, Error):
        self.Name = Name
        self.Error = Error

    fields = ('Name', 'Error')
