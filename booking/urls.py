
from django.urls import path
from . import views
from server import router

urlpatterns = [
    path('book', views.book, name='book'),
    path('get-all-bookings', views.get_all_bookings, name='get-all'),
    path('consumer-bookings/<int:id>', views.get_by_consumer, name='get-by-consumer'),
    path('provider-bookings/<int:id>', views.get_by_provider, name='get-by-provider'),
]
