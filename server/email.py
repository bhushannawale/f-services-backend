from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from django.core.mail import EmailMessage
from booking import serializer
from . import settings

@api_view(['POST'])
def send_email(request):
    try:
        mail = EmailMessage(request.data['subject'], request.data['message'], settings.EMAIL_HOST_USER, [ request.data['to'] ])
        mail.content_subtype = "html"
        mail.send()
        err = serializer.ErrorSerializer("Success", "Email has been sent")
        return JsonResponse({err.Name: err.Error})
    except:
        err = serializer.ErrorSerializer("Error", "Email could not send")
        return JsonResponse({err.Name: err.Error})
