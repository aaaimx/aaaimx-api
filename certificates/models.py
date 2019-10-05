from django.db import models
from uuid import uuid4
from datetime import datetime

# Create your models here.
class Certificate(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    description = models.TextField(default="", blank=True)
    to = models.CharField(max_length=100)
    qr_url = models.CharField(max_length=100)
    file = models.FileField(default="", blank=True, upload_to='certs')