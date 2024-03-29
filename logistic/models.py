from django.db import models
from uuid import uuid4
from datetime import datetime
from productivity.models import Division
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.


class TimeFieldsMixin(models.Model):

    # timestamp fields
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Event(models.Model):
    def __str__(self):
        return self.title
    title = models.TextField(default="", blank=True)
    corum = models.IntegerField(default=0, null=True, blank=True)
    hours = models.IntegerField(default=0, null=True, blank=True)
    is_draft = models.BooleanField(default=True)
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
    event = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.SET_NULL)
    published = models.BooleanField(default=False)
    to = models.CharField(max_length=100, blank=True, default="")
    QR = models.CharField(max_length=100, blank=True,
                          default='www.aaaimx.org/certificates/?id=')
    file = models.CharField(max_length=200, blank=True, default="")
    ftp_folder = models.CharField(max_length=50, blank=True, default="")
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(
        default=datetime.now, blank=True, null=True)


class Participant(TimeFieldsMixin):
    def __str__(self):
        return self.fullname

    # person fields
    fullname = models.CharField(default="", blank=True, max_length=200)
    email = models.EmailField(default="", blank=True, max_length=200)
    phone = models.CharField(default="", blank=True, max_length=20)
    ocupation = models.CharField(default="", blank=True, max_length=50)
    gender = models.CharField(default="", blank=True, max_length=50)

    # school fields
    enrollment = models.CharField(
        max_length=100, default="", null=True, blank=True)
    department = models.CharField(
        max_length=100, default="", null=True, blank=True)
    career = models.CharField(
        max_length=100, default="", null=True, blank=True)
    adscription = models.CharField(
        max_length=100, default="", null=True, blank=True)

    # management fields
    event = models.ForeignKey(
        Event, null=True, related_name='participants', blank=True, on_delete=models.CASCADE)
    is_responsible = models.BooleanField(default=False)
    cc_hours = models.IntegerField(default=0, blank=True)
