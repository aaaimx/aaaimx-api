from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Partner)
class AdminPartner(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'alias', 'type', 'logo')
    list_filter = ('type',)

@admin.register(Role)
class AdminRole(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('id','name')

@admin.register(Line)
class AdminLine(admin.ModelAdmin):
    list_display = ('id','topic')
    list_filter = ('id','topic')

@admin.register(Division)
class AdminDivision(admin.ModelAdmin):
    list_display = ('id','name', 'logo', 'story')
    list_filter = ('id','name')

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('title','start', 'end', 'responsible',)
    list_filter = ('responsible', 'start', 'end', 'lines')


@admin.register(Research)
class AdminResearch(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', 'projects', 'autors', 'lines')


@admin.register(Thesis)
class AdminThesis(admin.ModelAdmin):
    list_display = ('research', 'year',  'grade','resume')
    list_filter = ('grade', 'advisors')
    search_fields = ('research',)

@admin.register(Presentation)
class AdminPresentation(admin.ModelAdmin):
    list_display = ('research', 'year', 'event', 'resume')
    list_filter = ('event',)
    search_fields = ('research',)

@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('research', 'year', 'published_in', 'type', 'link', 'resume',)
    list_filter = ('published_in','type',)
    search_fields = ('research',)

@admin.register(Member)
class AdminMember(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'active', 'charge', 'adscription')
    list_filter = ('active', 'divisions', 'charge', 'roles', 'adscription')
    search_fields = ('fullname', 'charge',)