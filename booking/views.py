
from . import serializer
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import Booking
from consumer.models import Consumer
from provider.models import Provider
from server import err as errors


@api_view(['POST'])
def book(request):
    try:
        serialized = serializer.BookingSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data)
        else:
            return Response(serialized.errors)
    except:
        err = errors.ErrorSerializer("Error", "Data Error")
        return JsonResponse({err.Name: err.Error})



@api_view(['GET'])
def get_all_bookings(request):
    try:
        bookings = Booking.objects.all().order_by('-booking_time')
        res_list = []
        for b in bookings:
            serialized = serializer.BookingSerializer(b)
            res_list.append(serialized.data)
        return Response(res_list)
    except:
        err = errors.ErrorSerializer("Error", "Database Fetching Error")
        return JsonResponse({err.Name: err.Error})


@api_view(['GET'])
def get_by_consumer(request, id):
    try:
        consumer = Consumer.objects.get(id=id, delete_status=False)
        res_list = []
        bookings = Booking.objects.filter(consumer=consumer).order_by('-booking_time')
        for b in bookings:
            serialized = serializer.BookingSerializer(b)
            res_list.append(serialized.data)
        return Response(res_list)
    except:
        err = errors.ErrorSerializer("Error", "Consumer not exists")
        return JsonResponse({err.Name: err.Error})


@api_view(['GET'])
def get_by_provider(request, id):
    try:
        provider = Provider.objects.filter(id=id, delete_status=False)
        res_list = []
        bookings = Booking.objects.filter(provider=provider).order_by('-booking_time')
        for b in bookings:
            serialized = serializer.BookingSerializer(b)
            res_list.append(serialized.data)
        return Response(res_list)
    except:
        err = errors.ErrorSerializer("Error", "Provider not exists")
        return JsonResponse({err.Name: err.Error})
