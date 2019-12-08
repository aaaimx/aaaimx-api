from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta
from productivity.models import Member
# Create your models here.
class BankMovement(models.Model):
    to = models.CharField(default="", max_length=100, blank=True)
    origin = models.CharField(default="", max_length=100, blank=True)
    concept = models.TextField(default="", blank=True)
    amount = models.FloatField(default=0, blank=True)
    type = models.CharField(default="", max_length=100, blank=True)


class Membership(models.Model):
    income = models.ForeignKey(BankMovement, null=True, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL)
    uuid = models.UUIDField(default=uuid4, editable=False)
    QR = models.URLField(default="", max_length=100, blank=True)
    exp = models.DateTimeField(default=datetime.now() + timedelta(days=1) , blank=True)
