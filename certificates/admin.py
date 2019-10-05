from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Certificate)
class AdminCertifcate(admin.ModelAdmin):
    list_display = ('uuid', 'date_created', 'description', 'to', 'qr_url', 'file')
    list_filter = ('date_created', 'to',)