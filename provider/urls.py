
from django.urls import path
from . import views
from server import router

urlpatterns = [
    path('get-all-providers', views.get_all_providers, name='get-all'),
    path('get-provider/<int:id>', views.get_one, name='get-one'),
    path('create-provider', views.create_provider, name='create'),
    path('update-provider/<int:id>', views.update_provider, name='update'),
    path('delete-provider/<int:id>', views.delete_provider, name='delete'),
    path('login-provider', views.login, name='login'),
]