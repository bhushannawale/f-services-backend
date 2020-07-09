
from django.contrib import admin
from django.urls import include, path
from . import email
from . import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('provider.urls')),
    path('', include('consumer.urls')),
    path('', include('booking.urls')),
    path('', include('request.urls')),
    path('email', email.send_email),
    path('decode-token', auth.authenticate),
]
