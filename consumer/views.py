
from rest_framework import status
from .models import Consumer
from . import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from server import auth
from django.contrib.auth.hashers import make_password, check_password
from server import err as errors

@api_view(['GET'])
def get_all_consumers(request):
    try:
        result = Consumer.objects.all()
        res_list = []
        for r in result:
            serialized = serializer.ConsumerSerializer(r)
            res_list.append(serialized.data)
        return Response(res_list)
    except :
        err = errors.ErrorSerializer("Error", "Database Fetching Error")
        return JsonResponse({err.Name:err.Error})


@api_view(['GET'])
def get_one(request, id):
    try:
        consumer = Consumer.objects.get(id=id, delete_status=False)
        serialized = serializer.ConsumerSerializer(consumer)
        return Response(serialized.data)
    except :
        err = errors.ErrorSerializer("Error", "User Not Exists")
        return JsonResponse({err.Name:err.Error})


@api_view(['POST'])
def create_consumer(request):
    try:
        serialized = serializer.ConsumerSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save(password=make_password(request.data['password']))
            return Response(serialized.data)
        else:
            err = errors.ErrorSerializer("Error", serialized.errors)
            return JsonResponse({err.Name:err.Error})
    except :
        err = errors.ErrorSerializer("Error", "Data Error")
        return JsonResponse({err.Name:err.Error})


@api_view(['PUT'])
def update_consumer(request, id):
    try:
        serialized = serializer.ConsumerSerializer(data=request.data)
        if serialized.is_valid():
            if Consumer.objects.get(id=id, delete_status=False):
                consumer = Consumer.objects.get(id=id)
                serialized.update(consumer, serialized.data)
                return Response(serialized.data)
            else:
                err = errors.ErrorSerializer("Error", "User Not Exists")
                return JsonResponse({err.Name:err.Error})
        else:
            return Response(serialized.errors)
    except :
        err = errors.ErrorSerializer("Error", "Data Error")
        return JsonResponse({err.Name:err.Error})

@api_view(['DELETE'])
def delete_consumer(request, id):
    try :
        consumer = Consumer.objects.get(id=id, delete_status=False)
        consumer.delete_status = True
        consumer.save()
        return Response(serializer.ConsumerSerializer(consumer).data)
    except :
        err = errors.ErrorSerializer("Error", "User Not Exists")
        return JsonResponse({err.Name:err.Error})

@api_view(['POST'])
def login(request):
    try:
        email = request.data['email']
        password = request.data['password']
        if Consumer.objects.get(email=email, delete_status=False):
            consumer = Consumer.objects.get(email=email, delete_status=False)
            if check_password(password, consumer.password):
                token = auth.create_token('consumer', consumer.id, consumer.email)
                return JsonResponse({'Token': token.decode('utf-8')})
            else:
                err = errors.ErrorSerializer("Error", "Email or Password is incorrect")
                return JsonResponse({err.Name:err.Error})
        else:
            err = errors.ErrorSerializer("Error", "User Not Exists")
            return JsonResponse({err.Name:err.Error})
    except :
        err = errors.ErrorSerializer("Error", "Data Error")
        return JsonResponse({err.Name:err.Error})