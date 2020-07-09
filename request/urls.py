
from django.urls import path
from . import views
from server import router

urlpatterns = [
    path('add-request/<int:request_id>', views.same_request, name='add-one'),
    path('create-request', views.create_request, name='create'),
    path('get-all-requests', views.get_all_requests, name='get-all'),
    path('get-request-by-consumer/<int:id>', views.get_requests_by_consumer, name='get-by-consumer'),
    path('get-request-by-provider/<int:id>', views.get_requests_by_provider, name='get-by-provider'),
    path('accept-request/<int:id>', views.accept_request, name='accept'),
    path('delete-request/<int:id>', views.delete_request_by_id, name='delete'),
]