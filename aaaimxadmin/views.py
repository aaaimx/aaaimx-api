from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

# ViewSets define the view behavior.
from django.http.response import HttpResponse
from PIL import Image
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def LOCATION(file): return os.path.join(BASE_DIR, file)
def image(request):
    # ... create/load image here ...
    image = Image.open(LOCATION("utils/certificate.png"))
    # serialize to HTTP response
    response = HttpResponse(content_type="image/png")
    #response['Content-Length'] = str(len(response.content))
    image.save(response, 'PNG')
    return response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request):
        return Response({'message': 'This action is not available'}, status=405)

    def update(self, request, pk=None):
        return Response({'message': 'This action is not available'}, status=405)

    def partial_update(self, request, pk=None):
        return Response({'message': 'This action is not available'}, status=405)

    def destroy(self, request, pk=None):
        return Response({'message': 'This action is not available'}, status=405)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

