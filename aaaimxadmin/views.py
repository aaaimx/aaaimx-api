from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

# ViewSets define the view behavior.


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

