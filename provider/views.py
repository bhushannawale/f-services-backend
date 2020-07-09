
from rest_framework import status
from .models import Provider
from . import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from server import auth
from django.contrib.auth.hashers import make_password, check_password


@api_view(['GET'])
def get_all_providers(request):
    try :
        result = Provider.objects.all()
        res_list = []
        for r in result:
            serialized = serializer.ProviderSerializer(r)
            res_list.append(serialized.data)
        return Response(res_list)
    except :
        err = serializer.ErrorSerializer("Error","Database fetching error")
        return JsonResponse({err.Name:err.Error})



@api_view(['GET'])
def get_one(request, id):
    try :
        provider = Provider.objects.get(id=id, delete_status=False)
        serialized = serializer.ProviderSerializer(provider)
        return Response(serialized.data)
    except :
        err = serializer.ErrorSerializer("Error","Provider Not Exists")
        return JsonResponse({err.Name:err.Error})


@api_view(['POST'])
def create_provider(request):
    try :
        serialized = serializer.ProviderSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save(password=make_password(request.data['password']))
            return JsonResponse(serialized.data)
        else:
            return Response(serialized.errors)
    except :
        err = serializer.ErrorSerializer("Error","Data Error")
        return JsonResponse({err.Name:err.Error})


@api_view(['PUT'])
def update_provider(request, id):
    try :
        serialized = serializer.ProviderSerializer(data=request.data)
        if serialized.is_valid():
            if Provider.objects.get(id=id, delete_status=False) :
                provider = Provider.objects.get(id=id)
                serialized.update(provider, serialized.data)
                return Response(serialized.data)
            else :
                err = serializer.ErrorSerializer("Error","User not exists")
                return JsonResponse({err.Name:err.Error})
        else:
            return Response(serialized.errors)
    except :
        err = serializer.ErrorSerializer("Error","Data Error")
        return JsonResponse({err.Name:err.Error})

@api_view(['DELETE'])
def delete_provider(request, id):
    try :
        provider = Provider.objects.get(id=id, delete_status=False)
        provider.delete_status = True
        provider.save()
        return Response(serializer.ProviderSerializer(provider).data)
    except :
        err = serializer.ErrorSerializer("Error","User not exists")
        return JsonResponse({err.Name:err.Error})


@api_view(['POST'])
def login(request):
    try:
        email = request.data['email']
        password = request.data['password']
        if Provider.objects.get(email=email, delete_status=False):
            provider = Provider.objects.get(email=email, delete_status=False)
            if check_password(password, provider.password):
                token = auth.create_token('provider', provider.id, provider.email)
                return JsonResponse({'Token': token.decode('utf-8')})
            else:
                err = serializer.ErrorSerializer("Error", "Email or Password is incorrect")
                return JsonResponse({err.Name:err.Error})
        else:
            err = serializer.ErrorSerializer("Error","User not exists")
            return JsonResponse({err.Name:err.Error})
    except:
        err = serializer.ErrorSerializer("Error","Data Error")
        return JsonResponse({err.Name:err.Error})
