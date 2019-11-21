from django.db import models
from uuid import uuid4
from datetime import datetime
from productivity.models import *
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.
class Event(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100, null=True, default="")
    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    description = models.TextField(default="", blank=True)
    type = models.CharField(max_length=100)
    division = models.ForeignKey(Division, null=True, on_delete=models.SET_NULL)
    place = models.CharField(max_length=100)
    flyer = models.ImageField(
        default=None, null=True, blank=True, upload_to='flyers')

class Certificate(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(default="", blank=True)
    to = models.CharField(max_length=100)
    qr_url = models.CharField(max_length=100)
    file = models.FileField(upload_to='maps', storage=gd_storage)


class Component(models.Model):
    def __str__(self):
        return self.description
    description = models.CharField(default="", max_length=200, blank=True)
    stock = models.IntegerField(default=0, blank=True)
    available = models.IntegerField(default=0, blank=True)
    observations = models.TextField(default="", blank=True)
