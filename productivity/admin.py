from django.contrib import admin
from .models import *


@admin.register(Division)
class AdminDivision(admin.ModelAdmin):
    list_display = ('name', 'logo', 'fanpage')
    list_filter = ('name',)


# @admin.register(Member)
# class AdminMember(admin.ModelAdmin):
#     list_display = ('name', 'surname', 'active', 'board', 'committee', 'charge', 'roles', 'adscription', 'thumbnailFile')
#     list_filter = ('active', 'divisions', 'charge', 'roles', 'adscription')
#     search_fields = ('name', 'surname', 'charge',)
#     actions = ['mark_as_committee',]
#     list_per_page = 10

#     def mark_as_committee(self, request, queryset):
#         queryset.update(committee=True)
#     mark_as_committee.short_description = "Mark selected members as committee"
