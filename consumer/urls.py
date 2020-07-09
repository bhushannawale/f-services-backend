
from django.urls import path
from . import views
from server import router

urlpatterns = [
    path('get-all-consumers', views.get_all_consumers, name='get-all'),
    path('get-consumer/<int:id>', views.get_one, name='get-one'),
    path('create-consumer', views.create_consumer, name='create'),
    path('update-consumer/<int:id>', views.update_consumer, name='update'),
    path('delete-consumer/<int:id>', views.delete_consumer, name='delete'),
    path('login-consumer', views.login, name='login'),
]