from django.db import models
from consumer.models import Consumer
from provider.models import Provider

class Booking(models.Model):
    consumer        =       models.ForeignKey(Consumer, on_delete=models.DO_NOTHING)
    provider        =       models.ForeignKey(Provider, on_delete=models.DO_NOTHING)
    description     =       models.CharField(max_length=500)
    amount          =       models.PositiveIntegerField()
    booking_time    =       models.DateTimeField(auto_now_add=True, blank=False)


def __str__(self):
  return self.title
