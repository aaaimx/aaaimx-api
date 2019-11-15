from .models import Membership
from rest_framework import viewsets
from .serializers import MembershipSerializer

# ViewSets define the view behavior.
class MembershipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Memberships to be viewed or edited.
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
