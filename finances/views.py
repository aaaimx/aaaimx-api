

from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.
class MembershipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Memberships to be viewed or edited.
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

class BankMovementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BankMovements to be viewed or edited.
    """
    queryset = BankMovement.objects.all()
    serializer_class = MembershipSerializer