
from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=20)
    Error = serializers.CharField(max_length=254)
    def __init__(self, Name, Error):
        self.Name = Name
        self.Error = Error

    fields = ('Name', 'Error')