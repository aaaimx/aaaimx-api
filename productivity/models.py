from django.db import models
from uuid import uuid4
from datetime import datetime
from django_mysql.models import ListTextField


class Role(models.Model):
    id = models.CharField(default="", editable=True, max_length=100, primary_key=True, unique=True)

class Partner(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=True)
    name = models.CharField(default="", editable=True, max_length=200, primary_key=True, unique=True)
    alias = models.CharField(max_length=100)
    logo = models.ImageField(
        default=None, null=True, upload_to='logos')
    type = models.CharField(max_length=100, default="")
# fullname = models.CharField(default="", primary_key=True, unique=True, max_length=200)
# adscription = models.ForeignKey(Partner, null=True, on_delete=models.SET_NULL)
class Member(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=True)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    fullname = models.CharField(default="", primary_key=True, unique=True, max_length=200)
    email = models.CharField(default="", max_length=100)
    division = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    roles = ListTextField(
        base_field=models.CharField(max_length=50),
        size=10,
    )
    charge = models.CharField(max_length=100)
    adscription = models.ForeignKey(Partner, null=True, on_delete=models.SET_NULL)

class Project(models.Model):
    pass

class Research(models.Model):
    pass

class Line(models.Model):
    pass

