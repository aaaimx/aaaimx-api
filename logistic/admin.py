from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Certificate)
class AdminCertifcate(admin.ModelAdmin):
    list_display = ('uuid', 'type', 'to', 'QR', 'file', 'description')
    list_filter = ('type', 'to',)
    search_fields = ('to', 'description')
    list_per_page = 10

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end',  'description', 'type', 'division', 'flyer')
    list_filter = ('date_start', 'type', 'division')

@admin.register(Component)
class AdminComponent(admin.ModelAdmin):
    list_display = ('description', 'stock', 'available', 'observations')
    list_filter = ('stock', 'available')