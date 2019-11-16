from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from .models import *
import re
# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        limit = int(request.GET.get('limit', 10))
        offset = int(request.GET.get('offset', 0))
        page = int(request.GET.get('page', 1))
        fullname = request.GET.get('fullname', "")
        active = request.GET.get('active', None)

        # get all and order by fullname
        matched = Member.objects.all().order_by('fullname')

        # filter by fullname
        matched = list(filter(lambda m: re.findall(fullname.capitalize(), m.fullname), matched))

        # filter by status
        if active == "true":
            matched = list(filter(lambda m: m.active, matched))
        elif active == "false":
            matched = list(filter(lambda m: not m.active, matched))

        # pagination
        queryset = matched[offset:limit*page]

        # serialize data
        serializer = MemberSerializer(queryset, many=True)

        # custom response 
        # status code 200 OK
        return Response(data={
          'count': len(matched),
          'params': request.GET,
          'results': serializer.data})



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

class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lines to be viewed or edited.
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer

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