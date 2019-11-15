from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-date_joined')
    serializer_class = MemberSerializer

    def retrieve(self, request, pk=None):
        pass

class PartnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Partners to be viewed or edited.
    """
    queryset = Partner.objects.all().order_by('-name')
    serializer_class = PartnerSerializer

class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows divisions to be viewed or edited.
    """
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ResearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows research to be viewed or edited.
    """
    queryset = Research.objects.all().order_by('-title')
    serializer_class = ResearchSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class PresentationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows presentations to be viewed or edited.
    """
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer

class ThesisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows theses to be viewed or edited.
    """
    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializer