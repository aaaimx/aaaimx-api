from django.db import models
from uuid import uuid4
from datetime import datetime, timedelta
from productivity.models import Member
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.
class BankMovement(models.Model):
    def __str__(self):
        return '{0}: ${1} - {2}'.format(self.type, self.amount, self.origin)
    to = models.CharField(default="", max_length=100, blank=True)
    origin = models.CharField(default="", max_length=100, blank=True)
    concept = models.TextField(default="", blank=True)
    amount = models.FloatField(default=0, blank=True)
    type = models.CharField(default="", max_length=100, blank=True)
    voucher = models.FileField(upload_to='vouchers/%Y-%m-%D/', blank=True, storage=gd_storage)



class Membership(models.Model):
    def __str__(self):
        return self.display_name
    member = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL)
    display_name = models.CharField(default="", max_length=200, blank=True)
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    QR = models.URLField(default="", max_length=100, blank=True)
    exp = models.DateTimeField(default=datetime.now() + timedelta(days=1), blank=True)
    file = models.ImageField(upload_to='memberships', blank=True, storage=gd_storage)