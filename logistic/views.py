from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.decorators import action
from django.db.models import Q
from utils.images import generate_cert, LOCATION
from .forms import CertFile
import re
from storage.main import AAAIMXStorage

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-date_start')
    serializer_class = EventSerializer

# ViewSets define the view behavior.
class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Certificates to be viewed or edited.
    """
    queryset = Certificate.objects.all().order_by('-created_at')
    serializer_class = CertificateSerializer

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        to = request.GET.get('to', "")
        event = request.GET.get('event', None)
        type = request.GET.get('type', "")
        status = request.GET.get('status', None)
        _all = request.GET.get('all', None)

        self.queryset = self.queryset.filter(Q(to__icontains=to))
        if event is not None:
            self.queryset = self.queryset.filter(event__exact=event)
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

    def generate_cert(self, serializer, host):
        uuid = serializer.data['uuid']
        to = serializer.data['to']
        type = serializer.data['type']
        url = 'https://www.aaaimx.org/certificates/?id={0}'.format(uuid)
        imgCert = generate_cert(to, type, uuid, url)
        inst = Certificate.objects.filter(pk=uuid).update(QR=url)
        inst = Certificate.objects.get(pk=uuid)
        inst.file = host + '/image/'
        inst.save()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.generate_cert(serializer, request.scheme + '://' + request.META['HTTP_HOST'])
        return Response(serializer.data, status=201)

    def perform_create(self, serializer):
        serializer.save()


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Certificate.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=False)
        serializer.save()
        if not request.FILES.get('file', None):
            self.generate_cert(serializer, request.scheme + '://' + request.META['HTTP_HOST'])
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def upload(self, request, pk=None):
        instance = Certificate.objects.get(pk=pk)
        file = request.FILES['file']
        path = request.POST['upload'] + f'/{instance.type}/' + str(instance.uuid) + '.' + file.name.split('.')[1]
        ftp = AAAIMXStorage()
        ftp.login()
        ftp.save(file, path)
        ftp.exit()
        instance.file = 'https://www.aaaimx.org/' + path
        instance.save()
        return Response({})

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
