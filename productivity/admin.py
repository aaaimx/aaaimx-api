from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Partner)
class AdminPartner(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'alias', 'type', 'site', 'logoFile')
    list_filter = ('type',)
    list_per_page = 10

# @admin.register(Role)
# class AdminRole(admin.ModelAdmin):
#     list_display = ('name',)
#     list_filter = ('name',)

@admin.register(Line)
class AdminLine(admin.ModelAdmin):
    list_display = ('topic',)
    list_filter = ('topic',)
    list_per_page = 10

@admin.register(Division)
class AdminDivision(admin.ModelAdmin):
    list_display = ('name', 'logo', 'story')
    list_filter = ('name',)

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('title','start', 'end', 'responsible', 'lines')
    list_filter = ('responsible', 'start', 'end', 'lines')
    list_per_page = 10

@admin.register(Research)
class AdminResearch(admin.ModelAdmin):
    list_display = ('title', "year", "type",)
    list_filter = ('lines', "year", "type")
    search_fields = ('title',)
    list_per_page = 10

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('member', 'position', 'research')
    list_filter = ('member', 'position', 'research')
    list_per_page = 10

@admin.register(Advisor)
class AdminAdvisor(admin.ModelAdmin):
    list_display = ('member', 'position', 'research')
    list_filter = ('member', 'position', 'research')
    list_per_page = 10


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