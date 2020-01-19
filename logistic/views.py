from .models import Certificate
from rest_framework import viewsets
from .serializers import CertificateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.db.models import Q
from utils.images import generate_cert, LOCATION
from .forms import CertFile
import re

# ViewSets define the view behavior.
class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Certificates to be viewed or edited.
    """
    queryset = Certificate.objects.all().order_by('to')
    serializer_class = CertificateSerializer

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        to = request.GET.get('to', "")
        query = request.GET.get('query', "")
        type = request.GET.get('type', "")
        status = request.GET.get('status', None)
        _all = request.GET.get('all', None)

        self.queryset = self.queryset.filter(Q(to__icontains=to))
        if query:
            self.queryset = self.queryset.filter(description__icontains=query)
        if type:
            self.queryset = self.queryset.filter(type=type)

        # filter by status
        if status:
            self.queryset = self.queryset.filter(published=status.capitalize())

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def generate_cert(self, serializer):
        uuid = serializer.data['uuid']
        to = serializer.data['to']
        type = serializer.data['type']
        url = 'http://www.aaaimx.org/certificates/?id={0}'.format(uuid)
        imgCert = generate_cert(to, type, uuid, url)
        inst = Certificate.objects.filter(pk=uuid).update(QR=url)
        inst = Certificate.objects.get(pk=uuid)
        cert = CertFile(files={'file': imgCert }, instance=inst)
        if cert.is_valid():
            cert.save(commit=False)
            cert.save()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.generate_cert(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        print(partial)
        instance = Certificate.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if not request.FILES.get('file', None):
            self.generate_cert(serializer)
            
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = Certificate.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
            
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)