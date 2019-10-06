from django.db import models

# Create your models here.
class Income(models.Model):
    from_what = models.CharField(default="", max_length=100, blank=True)
    concept = models.TextField(default="", blank=True)
    division = models.CharField(default="", max_length=100, blank=True)
    amount = models.FloatField(default=0, blank=True)
    type = models.TextField(default="", blank=True)

# Create your models here.
class Expense(models.Model):
    to = models.CharField(default="", max_length=100, blank=True)
    concept = models.TextField(default="", blank=True)
    division = models.CharField(default="", max_length=100, blank=True)
    amount = models.FloatField(default=0, blank=True)