from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Partner)
class AdminPartner(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'alias', 'type', 'logo')
    list_filter = ('type',)

@admin.register(Role)
class AdminRole(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)

# Register your models here.
@admin.register(Member)
class AdminMember(admin.ModelAdmin):
    list_display = ('fullname', 'active', 'division', 'charge', 'adscription')
    list_filter = ('active', 'division', 'charge', 'adscription')