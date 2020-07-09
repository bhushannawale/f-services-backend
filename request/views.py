
from . import serializer
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from consumer.models import Consumer
from provider.models import Provider
from consumer.serializer import ConsumerSerializer
from provider.serializer import ProviderSerializer
from .models import Request

@api_view(['POST'])
def create_request(request):
    try:
        req = serializer.RequestSerializer(data=request.data)
        if req.is_valid():
            req.save()
            return JsonResponse(req.data)
        else:
            return Response(req.errors)
    except :
        err = serializer.ErrorSerializer("Error", "Data Error")
        return JsonResponse({err.Name: err.Error})


@api_view(['PUT'])
def same_request(request, request_id):
    try:
        req = Request.objects.get(id=request_id)
        req.provider.add(request.data['provider'])
        req.save()
        serialized = serializer.RequestSerializer(req)
        return Response(serialized.data)
    except:
        err = serializer.ErrorSerializer("Error", "Data Error")
        return JsonResponse({err.Name: err.Error})


@api_view(['GET'])
def get_all_requests(request):
    try:
        requests = Request.objects.all()
        print(requests)
        req_list = []
        for r in requests:
            serialized = serializer.RequestSerializer(r)
            req_list.append(serialized.data)
        return Response(req_list)
    except:
        err = serializer.ErrorSerializer("Error", "Database Error")
        return JsonResponse({err.Name: err.Error})


@api_view(['GET'])
def get_requests_by_consumer(request, id):
    try:
        consumer = Consumer.objects.get(id=id, delete_status=False)
        requests = Request.objects.filter(consumer=consumer, status=False)
        req_list = []
        for r in requests:
            serialized = serializer.RequestSerializer(r)
            req_list.append(serialized.data)
        return Response(req_list)
    except:
        err = serializer.ErrorSerializer("Error", "Consumer not exists")
        return JsonResponse({err.Name: err.Error})


@api_view(['GET'])
def get_requests_by_provider(request, id):
    try:
        provider = Provider.objects.get(id=id, delete_status=False)
        requests = Request.objects.filter(provider=provider, status=False)
        req_list = []
        for r in requests:
            serialized = serializer.RequestSerializer(r)
            req_list.append(serialized.data)
        return Response(req_list)
    except:
        err = serializer.ErrorSerializer("Error", "Provider not exists")
        return JsonResponse({err.Name: err.Error})


@api_view(['PUT'])
def accept_request(request, id):
    try:
        req = Request.objects.get(id=id, status=False)
        req.status = True
        req.save()
        serialized = serializer.RequestSerializer(req)
        return Response(serialized.data)
    except:
        err = serializer.ErrorSerializer("Error", "Request not exists")
        return JsonResponse({err.Name: err.Error})

@api_view(['DELETE'])
def delete_request_by_id(request, id):
    try:
        req = Request.objects.get(id=id, status=True).delete()
        return Response({"Result": "Request has been Deleted"})
    except:
        err = serializer.ErrorSerializer("Error", "Request not exists")
        return JsonResponse({err.Name: err.Error})