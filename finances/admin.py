from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Membership)
class AdminMembership(admin.ModelAdmin):
    list_display = ('uuid', 'display_name', 'file', 'exp',)
    list_filter = ('member', 'exp',)


@admin.register(Invoice)
class AdminInvoice(admin.ModelAdmin):
    list_display = ('origin',  'description',  'amount',   'type', 'created_at', 'voucher',)
    list_filter = ('origin',  'type', 'created_at')
