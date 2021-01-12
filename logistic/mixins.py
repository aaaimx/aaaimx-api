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


class DeepListModelMixin:
    """
    Apply this mixin to any view or viewset to get a deep 'list' action
    based on a `depth_serializer` attribute, aditionally to the default single field serializer_class.
    """

    def list(self, request, *args, **kwargs):
        self.filter_by_date_range(request)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.deep_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.deep_serializer(queryset, many=True)
        return Response(serializer.data)

    def filter_by_date_range(self, request):
        range = request.GET.getlist('range[]', None)
        if range:
            key = self.filter_date_field
            obj = {'%s__range' % key: range}
            self.queryset = self.queryset .filter(**obj)
