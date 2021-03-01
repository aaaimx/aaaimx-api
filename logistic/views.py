# standard library imports
import re
from datetime import date

# related third party imports
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

# local application/library specific imports
from utils.images import generate_cert
from storage.main import AAAIMXStorage
from .mixins import DateRangeFilterMixin
from .models import *
from .serializers import *


class DateRangeFilterBackend(filters.BaseFilterBackend):
    """
    Filter by date range using `filter_date_field` property
    """

    def filter_queryset(self, request, queryset, view):
        range = request.GET.getlist('range[]', None)
        if range:
            key = view.filter_date_field
            obj = {'%s__range' % key: range}
            return queryset.filter(**obj)
        return queryset


class CCFilterBackend(filters.BaseFilterBackend):
    """
    Filter by date range using `filter_date_field` property
    """

    def filter_queryset(self, request, queryset, view):
        isCC = request.GET.get('isCC')
        if view.action == 'list' and isCC:
            return queryset.filter(
                enrollment__isnull=False,
                cc_hours__gt=0,
                adscription='ITM')
        return queryset


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-date_start')
    serializer_class = EventSerializer
    filter_date_field = "date_start"
    filter_backends = [DjangoFilterBackend, OrderingFilter,
                       SearchFilter, DateRangeFilterBackend]

    filterset_fields = '__all__'
    search_fields = ['description', 'title', ]
    ordering_fields = '__all__'
    ordering = ['-date_start']

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSerializerDeep
        return EventSerializer

    @action(detail=False, methods=['GET'])
    def future(self, request):
        queryset = self.get_queryset().filter(
            date_start__gte=date.today(), is_draft=False)
        queryset = self.filter_queryset(queryset)
        serializer = EventSerializerDeep(queryset, many=True)
        return Response(serializer.data)


class ParticipantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Participants to be viewed or edited.
    """
    queryset = Participant.objects.all().order_by('-created_at')
    serializer_class = ParticipantSerializer
    filter_date_field = "created_at"
    filter_backends = [DjangoFilterBackend, OrderingFilter,
                       SearchFilter, CCFilterBackend, DateRangeFilterBackend]
    filterset_fields = ['event', 'career', 'department', 'adscription']
    search_fields = ['fullname', 'career', 'department', 'adscription']
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'list':
            return ParticipantSerializerDeep
        return ParticipantSerializer

    @action(detail=False, methods=['POST', 'GET'], permission_classes=[], authentication_classes=[])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Certificates to be viewed or edited.
    """
    queryset = Certificate.objects.all().order_by('-created_at')
    serializer_class = CertificateSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter,
                       SearchFilter, DateRangeFilterBackend]
    filter_date_field = "created_at"

    filterset_fields = ['type', 'published', 'event']
    search_fields = ['type', 'description', 'to']
    ordering_fields = '__all__'
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return CertificateSerializerDeep
        return CertificateSerializer

    def get_queryset(self):
        if self.action == 'unasigned':
            return self.queryset.filter(event__isnull=True)
        return self.queryset

    @action(detail=False, methods=['GET'])
    def unasigned(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def upload_to_ftp(self, file, folder, filename):
        ftp = AAAIMXStorage()
        ftp.login()
        ftp.save(file, folder, filename)
        ftp.exit()

        return settings.FTP_BASE_URL + folder + filename

    def generate_cert(self, serializer):
        uuid = serializer.data['uuid']
        to = serializer.data['to']
        type = serializer.data['type']
        desc = serializer.data['description']
        QR = settings.FTP_BASE_URL + 'certificates/?id={0}'.format(uuid)
        file = generate_cert(to, type, desc, uuid, QR)
        instance = Certificate.objects.get(pk=uuid)
        folder = '%s/%s/' % (instance.ftp_folder, instance.type)
        filename = '%s.jpg' % str(instance.uuid)
        url = self.upload_to_ftp(file, folder, filename)
        instance.description = desc
        instance.QR = QR
        instance.file = url
        instance.save()
        return Response({})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.generate_cert(serializer)
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Certificate.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=False)
        serializer.save()
        if not request.FILES.get('file', None):
            self.generate_cert(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def upload(self, request, pk=None):
        instance = Certificate.objects.get(pk=pk)
        file = request.FILES['file']
        ftp_folder = request.POST['ftp_folder']
        folder = '%s/%s/' % (ftp_folder, instance.type)
        filename = '%s.jpg' % str(instance.uuid)
        url = self.upload_to_ftp(file, folder, filename)
        instance.file = url
        instance.ftp_folder = ftp_folder
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        folder = '%s/%s' % (instance.ftp_folder, instance.type)
        ftp = AAAIMXStorage()
        ftp.login()
        ftp.remove(folder, str(instance.uuid) + '.jpg')
        ftp.exit()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
