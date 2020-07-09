from django.db import models
from consumer.models import Consumer
from provider.models import Provider

class Request(models.Model):
  consumer        =       models.ForeignKey(Consumer, on_delete=models.CASCADE)
  provider        =       models.ManyToManyField(Provider)
  description     =       models.CharField(max_length=500)
  status          =       models.BooleanField(default=False)
  request_time    =       models.DateTimeField(auto_now_add=True, blank=False)

def __str__(self):
  return self.title
