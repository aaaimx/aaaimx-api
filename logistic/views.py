from .models import *
from rest_framework import viewsets
from .serializers import *
from .mixins import DeepListModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.decorators import action
from django.db.models import Q
from django.shortcuts import get_object_or_404
from utils.images import generate_cert, LOCATION
from .forms import CertFile
import re
from storage.main import AAAIMXStorage
from datetime import date
from bs4 import BeautifulSoup
from django.conf import settings

class EventViewSet(DeepListModelMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-date_start')
    serializer_class = EventSerializer
    deep_serializer = EventSerializerDeep

    filterset_fields = ['type', 'published', 'place']
    search_fields = ['type', 'description', 'title', 'place']
    ordering_fields = '__all__'
    ordering = ['-date_start']

    @action(detail=False, methods=['GET'])
    def future(self, request):

        queryset = self.get_queryset().filter(date_start__gte=date.today())
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = EventSerializerDeep(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EventSerializerDeep(queryset, many=True)
        return Response(serializer.data)


class ParticipantViewSet(DeepListModelMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows Participants to be viewed or edited.
    """
    queryset = Participant.objects.all().order_by('-created_at')
    serializer_class = ParticipantSerializer
    deep_serializer = ParticipantSerializerDeep

    filterset_fields = ['event', 'career', 'department', 'adscription']
    search_fields = ['career', 'department', 'adscription']
    ordering_fields = '__all__'

    @action(detail=False, methods=['POST', 'GET'], permission_classes=[], authentication_classes=[])
    def register(self, request, *args, **kwargs):
        enrollment = request.data.get('enrollment', None)
        event_id = request.data.get('event', None)
        event = get_object_or_404(Event, pk=event_id)
        p = Participant.objects.filter(event=event, enrollment=enrollment)

        if (len(p)):
            return Response({
                'detail': 'Already registered'
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CertificateViewSet(DeepListModelMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows Certificates to be viewed or edited.
    """
    queryset = Certificate.objects.all().order_by('-created_at')
    serializer_class = CertificateSerializer
    deep_serializer = CertificateSerializerDeep

    filterset_fields = ['type', 'published', 'event']
    search_fields = ['type', 'description', 'to', 'event']
    ordering_fields = '__all__'
    ordering = ['-created_at']

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
        desc = BeautifulSoup('<p>%s</p>' %
                             serializer.data['description'], "xml").get_text()
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
