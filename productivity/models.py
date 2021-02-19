from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta
from django.contrib.postgres.fields import ArrayField, JSONField
from .mixins import TimeModelMixin

class Division(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=100, unique=True)
    story = models.TextField(default="", blank=True)
    logo = models.CharField(default="", max_length=100)


class Partner(models.Model):
    def __str__(self):
        return self.alias
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    name = models.CharField(default="", editable=True,
                            max_length=255, unique=True)
    alias = models.CharField(max_length=100, blank=True)
    site = models.URLField(default="", max_length=100, blank=True)
    logoName = models.CharField(max_length=100, blank=True)
    logoFile = models.CharField(
        max_length=100, blank=True, null=True, default="")
    type = models.CharField(max_length=100, default="")


class Member(TimeModelMixin):
    def __str__(self):
        return self.name + ' ' + self.surname
    name = models.CharField(default="", max_length=50)
    email = models.EmailField(default="", blank=True, max_length=100)

    username = models.CharField(max_length=50, default="", blank=True)
    active = models.BooleanField(default=True)
    roles = ArrayField(models.CharField(
        max_length=50, blank=True), size=20, blank=True, null=True, default=list)
    dateJoined = models.DateField(null=True, blank=True)

class Research(TimeModelMixin):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "research"

    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=True)
    title = models.TextField(default="", blank=False)
    tags = ArrayField(models.CharField(max_length=50, blank=True), size=20, blank=True, null=True, default=list)
    description = models.TextField(default="", blank=True)
    type = models.CharField(default="", max_length=30,blank=True, null=True)
    banner = models.URLField(max_length=200, blank=True, default="")

