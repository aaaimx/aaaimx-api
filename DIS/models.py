from django.db import models
from datetime import date
from django_mysql.models import ListCharField

# Create your models here.
class Pet(models.Model):
    def __str__(self):
        return self.nombre
    foto = models.URLField(blank=True, default="", max_length=200)
    nombre = models.CharField(max_length=100, default="")
    sexo = models.CharField(max_length=100, default="", blank=True)
    mes_ingreso = models.DateField(default=None, blank=True)
    esterilizado = models.BooleanField(default=False)
    edad = models.CharField(max_length=100, default="", blank=True)
    peso = models.CharField(max_length=100, default="", blank=True)
    descripcion = models.TextField(blank=True)
    vacunas = models.TextField(blank=True)