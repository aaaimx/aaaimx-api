from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'sexo', 'edad', 'peso', 'descripcion')
    list_filter = ('sexo', 'edad', 'peso',)