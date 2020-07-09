from django.db import models

class Provider(models.Model):
    first_name      =      models.CharField(max_length=120)
    last_name       =      models.CharField(max_length=120)
    address         =      models.CharField(max_length=254)
    pincode         =      models.CharField(max_length=6)
    email           =      models.EmailField(max_length=254)
    password        =      models.CharField(max_length=75)
    phone           =      models.CharField(max_length=10)
    service_type    =      models.CharField(max_length=10)
    base_price      =      models.PositiveIntegerField()
    rate_per_km     =      models.PositiveIntegerField(default=0)
    delete_status   =      models.BooleanField(default=False)


def __str__(self):
  return self.title
