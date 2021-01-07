from django.db import models
from uuid import uuid4
from datetime import datetime
from productivity.models import Division
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.


class Event(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100, null=True, default="")
    corum = models.IntegerField(default=0, null=True, blank=True)
    hours = models.IntegerField(default=0, null=True, blank=True)
    published = models.BooleanField(default=False)
    open_to_public = models.BooleanField(default=False)

    date_start = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    description = models.TextField(default="", blank=True)
    type = models.CharField(max_length=100, blank=True)
    division = models.ForeignKey(
        Division, null=True, blank=True, on_delete=models.SET_NULL)
    place = models.CharField(max_length=100, blank=True)
    flyer = models.URLField(
        default="", null=True, blank=True)


class Certificate(models.Model):
    def __str__(self):
        return '{0}: {1}'.format(self.type, self.to)
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    type = models.CharField(max_length=100, default="RECOGNITION", blank=True,)
    event = models.CharField(max_length=200, default="", blank=True, null=True)
    published = models.BooleanField(default=False)
    to = models.CharField(max_length=100, blank=True, default="")
    QR = models.CharField(max_length=100, blank=True,
                          default='www.aaaimx.org/certificates/?id=')
    file = models.CharField(max_length=200, blank=True, default="")
    ftp_folder = models.CharField(max_length=50, blank=True, default="")
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(
        default=datetime.now, blank=True, null=True)

# Certificate.objects.all().update(has_custom_file=True)

class Participant(models.Model):
    def __str__(self):
        return self.fullname
    fullname = models.CharField(default="", blank=True, max_length=200)
    email = models.EmailField(default="", blank=True, max_length=200)

    event = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.CASCADE)

    enrollment = models.CharField(
        max_length=100, default="", null=True, blank=True)
    department = models.CharField(
        max_length=100, default="", null=True, blank=True)
    career = models.CharField(
        max_length=100, default="", null=True, blank=True)
    adscription = models.CharField(
        max_length=100, default="", null=True, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    cc_hours = models.IntegerField(default=0, blank=True)
