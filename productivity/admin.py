from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Partner)
class AdminPartner(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'alias', 'type', 'logo')
    list_filter = ('type',)

@admin.register(Role)
class AdminRole(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

@admin.register(Line)
class AdminLine(admin.ModelAdmin):
    list_display = ('topic',)
    list_filter = ('topic',)

@admin.register(Division)
class AdminDivision(admin.ModelAdmin):
    list_display = ('name', 'logo', 'story')
    list_filter = ('name',)

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('title','start', 'end', 'responsible',)
    list_filter = ('responsible', 'start', 'end', 'lines')

@admin.register(Research)
class AdminResearch(admin.ModelAdmin):
    list_display = ('title', "resume", "year", "type")
    list_filter = ('title', 'projects', 'lines', "year", "type")
    search_fields = ('title',)

@admin.register(Advisor)
class AdminAdvisor(admin.ModelAdmin):
    list_display = ('member', 'position', 'research')
    list_filter = ('member', 'position',)


@admin.register(Member)
class AdminMember(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'active', 'charge', 'adscription')
    list_filter = ('active', 'divisions', 'charge', 'roles', 'adscription')
    search_fields = ('fullname', 'charge',)