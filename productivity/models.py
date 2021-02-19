from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta
from django.contrib.postgres.fields import ArrayField, JSONField
from .mixins import BaseAbstractModel

class Division(BaseAbstractModel):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=100, unique=True)
    logo = models.URLField(default="", max_length=200)
    color = models.CharField(default="", max_length=8)
    fanpage = models.URLField(default="", max_length=6)


class Member(BaseAbstractModel):
    def __str__(self):
        return self.name + ' ' + self.surname
    name = models.CharField(default="", max_length=50)
    email = models.EmailField(default="", blank=True, max_length=100)

    username = models.CharField(max_length=50, default="", blank=True)
    active = models.BooleanField(default=True)
    roles = ArrayField(models.CharField(
        max_length=50, blank=True), size=20, blank=True, null=True, default=list)
    dateJoined = models.DateField(null=True, blank=True)


