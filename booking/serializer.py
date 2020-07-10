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

