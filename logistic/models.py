from django.db import models
from uuid import uuid4
from datetime import datetime


# Create your models here.
class Event(models.Model):
    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    description = models.TextField(default="", blank=True)
    type = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    flyer = models.ImageField(
        default=None, null=True, upload_to='flyers')

class Certificate(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(default="", blank=True)
    to = models.CharField(max_length=100)
    qr_url = models.CharField(max_length=100)
    file = models.FileField(default="", blank=True, upload_to='certs')


class Stock(models.Model):
    description = models.TextField(default="", blank=True)
    amount = models.IntegerField(default=0, blank=True)
