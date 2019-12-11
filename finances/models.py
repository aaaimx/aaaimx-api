from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta
from productivity.models import Member
# Create your models here.
class BankMovement(models.Model):
    def __str__(self):
        return '{0}: ${1} - {2}'.format(self.type, self.amount, self.origin)
    to = models.CharField(default="", max_length=100, blank=True)
    origin = models.CharField(default="", max_length=100, blank=True)
    concept = models.TextField(default="", blank=True)
    amount = models.FloatField(default=0, blank=True)
    type = models.CharField(default="", max_length=100, blank=True)


class Membership(models.Model):
    def __str__(self):
        return '{0} {1}'.format(self.member.name, self.member.surname).upper()
    income = models.ForeignKey(BankMovement, null=True, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL)
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    QR = models.URLField(default="", max_length=100, blank=True)
    exp = models.DateTimeField(default=datetime.now() + timedelta(days=1) , blank=True)
