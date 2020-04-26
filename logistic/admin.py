from django.contrib import admin
from .models import *
from .mixins import ExportCsvMixin

# Register your models here.
@admin.register(Certificate)
class AdminCertifcate(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('QR', 'type', 'to',  'published',
                    'created_at', 'file', 'description')
    list_filter = ('type', 'created_at',)
    search_fields = ('to', 'description', 'created_at')
    ordering = ('-created_at',)
    actions = ['publish', 'export_as_csv']
    list_per_page = 10

    def publish(self, request, queryset):
        queryset.update(published=True)
    publish.short_description = "Publish selected certificates"

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end',  'description', 'type', 'division', 'flyer')
    list_filter = ('date_start', 'type', 'division')

@admin.register(Component)
class AdminComponent(admin.ModelAdmin):
    list_display = ('description', 'stock', 'available', 'observations')
    list_filter = ('stock', 'available')
