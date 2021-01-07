from django.contrib import admin
from .models import *
from .mixins import ExportCsvMixin

EVENT = "SINABIA 2019"

# Register your models here.
@admin.register(Certificate)
class AdminCertifcate(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('to', 'uuid', 'event',  'published', 'file', 'description')
    list_filter = ('event', 'type', 'published', 'created_at',)
    search_fields = ('to', 'description', 'created_at')
    ordering = ('-created_at',)
    # actions = ['change_file', 'export_as_csv', 'add']
    list_per_page = 10

    def add(self, request, queryset):
        queryset.update(event=EVENT)
    
    def change_file(self, request, queryset):
        for q in queryset:
            q.file = 'https://www.aaaimx.org/certificates/2019/' + q.type + '/' + str(q.uuid) + '.jpg'
            q.save()

    add.short_description = "Add a event: " + EVENT
    change_file.short_description = "Publish selected certificates"
    
@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    ordering = ('-date_start',)
    list_display = ('title', 'date_start', 'date_end',  'description', 'type', 'division')
    list_filter = ('date_start', 'type', 'division')


@admin.register(Participant)
class AdminParticipant(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('fullname', 'email', 'adscription',  'career', 'department', 'enrollment')
    