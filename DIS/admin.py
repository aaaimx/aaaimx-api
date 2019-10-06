from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    list_display = ('nombre', 'sexo', 'edad', 'peso', 'descripcion', 'foto')
    list_filter = ('sexo', 'edad', 'peso',)