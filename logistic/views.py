from .models import Certificate
from rest_framework import viewsets
from .serializers import CertificateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

# ViewSets define the view behavior.
class CertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Certificates to be viewed or edited.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        uuid = serializer.data['uuid']
        Certificate.objects.filter(pk=uuid).update(QR='www.aaaimx.org/certificates/?id={0}'.format(uuid))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
