from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from .models import *
import re
# Create your views here.
class MembershipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Memberships to be viewed or edited.
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

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
        page = self.paginate_queryset(matched)

         # serialize data
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



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
    queryset = Project.objects.all().order_by('title')
    serializer_class = ProjectSerializer

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        limit = int(request.GET.get('limit', 10))
        offset = int(request.GET.get('offset', 0))
        page = int(request.GET.get('page', 1))
        title = request.GET.get('title', "")
        institute = request.GET.get('institute', None)

        self.queryset = self.filter_queryset(self.get_queryset())

        # filter by title
        matched = list(filter(lambda m: re.findall(title.upper(), m.title.upper()), self.queryset))
        if institute:
            matched = list(filter(lambda m: m.institute.alias == institute, matched))

        # pagination
        queryset = matched[offset:limit*page]
        page = self.paginate_queryset(matched)

         # serialize data
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ResearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows research to be viewed or edited.
    """
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer

    def list(self, request, *args, **kwargs):
        # get query params
        limit = int(request.GET.get('limit', 10))
        offset = int(request.GET.get('offset', 0))
        page = int(request.GET.get('page', 1))
        year = request.GET.get('year', 0)
        title = request.GET.get('title', "")
        type = request.GET.get('type', None)

        self.queryset = self.filter_queryset(self.get_queryset())

        # filter by title
        matched = list(filter(lambda r: re.findall(title.upper(), r.title.upper()), self.queryset))
        if type:
            matched = list(filter(lambda r: r.type == type, matched))
        if year and year != 0 and year != "":
            matched = list(filter(lambda r: r.year == int(year), matched))

        # pagination
        queryset = matched[offset:limit*page]
        page = self.paginate_queryset(matched)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AdvisorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Advisors to be viewed or edited.
    """
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer