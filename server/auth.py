
from django.http.response import JsonResponse
from server import settings
import jwt
from rest_framework.decorators import api_view

def create_token(user, id, email):
    try:
        token = jwt.encode({ 'user': user, 'user_id': id, 'user_email': email}, settings.SECRET_KEY, algorithm='HS256')
        return token
    except:
        return JsonResponse({'Error': 'Data Error'})

@api_view(['GET'])
def authenticate(request):
    try:
        token = request.headers['Token']
        decode = jwt.decode(token, settings.SECRET_KEY, 'utf-8', algorithm='HS256')
        return JsonResponse({'id': decode['user_id'], 'email': decode['user_email']})
    except:
        return JsonResponse({'Error': 'Data Error'})
