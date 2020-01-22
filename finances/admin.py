from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Membership)
class AdminMembership(admin.ModelAdmin):
    list_display = ('uuid', 'display_name', 'file', 'exp',)
    list_filter = ('member', 'exp',)


@admin.register(BankMovement)
class AdminBankMovement(admin.ModelAdmin):
    list_display = ('id', 'origin', 'to',  'concept',  'amount', 'voucher',  'type', )
    list_filter = ('origin', 'amount', 'to',  'type',)
