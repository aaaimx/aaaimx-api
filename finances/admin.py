from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Membership)
class AdminMembership(admin.ModelAdmin):
    list_display = ('uuid', 'member', 'income', 'exp')
    list_filter = ('member', 'exp',)


@admin.register(BankMovement)
class AdminBankMovement(admin.ModelAdmin):
    list_display = ('id', 'origin', 'to',  'concept',  'amount',  'type', )
    list_filter = ('origin', 'amount', 'to',  'type',)
