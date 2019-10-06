from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Income)
class AdminIncome(admin.ModelAdmin):
    list_display = ('id', 'from_what' ,   'concept' ,    'division' ,   'amount' ,  'type' , )
    list_filter = ('from_what' ,   'division' ,   'amount' ,  'type' ,)

@admin.register(Expense)
class AdminExpense(admin.ModelAdmin):
    list_display = ('id', 'to' ,   'concept' ,    'division' ,   'amount' ,  )
    list_filter = ('to' ,   'division' ,   'amount' , )