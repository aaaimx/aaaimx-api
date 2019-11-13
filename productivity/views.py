from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemberSerializer, ResearchSerializer
from .models import Member, Research
# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-date_joined')
    serializer_class = MemberSerializer

class ResearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows research to be viewed or edited.
    """
    queryset = Research.objects.all().order_by('-title')
    serializer_class = ResearchSerializer