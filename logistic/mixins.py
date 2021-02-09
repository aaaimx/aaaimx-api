import csv
from django.http import HttpResponse


class ExportCsvMixin:

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"


class DateRangeFilterMixin:
    """
    Apply this mixin to any view or viewset to get a filtered 'list' action
    based on a `filter_date_field` attribute.
    """

    def get_queryset(self):
        range = self.request.GET.getlist('range[]', None)
        if self.action == 'list' and range:
            key = self.filter_date_field
            obj = {'%s__range' % key: range}
            return self.queryset.filter(**obj)
        return self.queryset
