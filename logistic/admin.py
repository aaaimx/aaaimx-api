from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Certificate)
class AdminCertifcate(admin.ModelAdmin):
    list_display = ('uuid', 'date_created', 'description', 'to', 'qr_url', 'file')
    list_filter = ('date_created', 'to',)

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end',  'description', 'type', 'division', 'flyer')
    list_filter = ('date_start', 'type', 'division')

@admin.register(Component)
class AdminComponent(admin.ModelAdmin):
    list_display = ('description', 'stock', 'available', 'observations')
    list_filter = ('stock', 'available')