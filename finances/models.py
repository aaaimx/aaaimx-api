from django.db import models
from uuid import uuid4
from datetime import datetime
from productivity.models import *

# Create your models here.
class Income(models.Model):
    origin = models.CharField(default="", max_length=100, blank=True)
    concept = models.TextField(default="", blank=True)
    division = models.ForeignKey(Division, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField(default=0, blank=True)
    type = models.TextField(default="", blank=True)

class Expense(models.Model):
    to = models.CharField(default="", max_length=100, blank=True)
    concept = models.TextField(default="", blank=True)
    division = models.ForeignKey(Division, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField(default=0, blank=True)

class Membership():
    uuid = models.UUIDField(default=uuid4, editable=True)