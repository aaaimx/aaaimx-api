from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse

from django.db.models import Q
from .serializers import *
from .models import *
import re
# Create your views here.


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.none()
    serializer_class = MemberSerializer

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        name = request.GET.get('name', "")
        active = request.GET.get('active', None)
        panel = request.GET.get('panel', None)
        _all = request.GET.get('all', None)
        order = 'charge'

        if panel == "true":
            self.queryset = Member.objects.filter(Q(name__icontains=name) | Q(
                surname__icontains=name), Q(committee=True) | Q(board=True)).order_by(order)
        else:
            self.queryset = Member.objects.filter(
                Q(name__icontains=name) | Q(surname__icontains=name)).order_by(order)

        # filter by status
        if active == "true":
            self.queryset = self.queryset.filter(active=True)
        elif active == "false":
            self.queryset = self.queryset.filter(active=False)

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        instance = Member.objects.get(pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Member.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @action(detail=False)
    def panel(self, request):
        panel_members = Member.objects.filter(Q(committee=True) | Q(board=True)
                                              ).order_by('-name')
        serializer = self.get_serializer(panel_members, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def divisions(self, request):
        division_members = Member.objects.all().order_by('-name')
        division_members = list(filter(lambda m: m.divisions.all() or m.board, division_members))
        serializer = self.get_serializer(division_members, many=True)
        return Response(serializer.data)

class PartnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Partners to be viewed or edited.
    """
    queryset = Partner.objects.all().order_by('-name')
    serializer_class = PartnerSerializer
    

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        name = request.GET.get('name', "")
        type = request.GET.get('type', None)
        _all = request.GET.get('all', None)

        self.queryset = self.queryset.filter(Q(name__icontains=name) | Q(
                alias__icontains=name))
        if type:
            self.queryset = self.queryset.filter(type=type)

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


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

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        _all = request.GET.get('all', None)

        self.queryset = self.filter_queryset(self.get_queryset())

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class DivisionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows divisions to be viewed or edited.
    """
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        _all = request.GET.get('all', None)

        self.queryset = self.filter_queryset(self.get_queryset())

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


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
        title = request.GET.get('title', "")
        institute = request.GET.get('institute', None)
        _all = request.GET.get('all', None)

        self.queryset = self.filter_queryset(self.get_queryset())

        # filter by title
        matched = list(filter(lambda m: re.findall(
            title.upper(), m.title.upper()), self.queryset))
        if institute:
            matched = list(
                filter(lambda m: m.institute.alias == institute, matched))

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(matched)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class ResearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows research to be viewed or edited.
    """
    queryset = Research.objects.all().order_by('-year')
    serializer_class = ResearchSerializer

    def list(self, request, *args, **kwargs):
        # get query params
        year = request.GET.get('year', 0)
        title = request.GET.get('title', "")
        type = request.GET.get('type', None)
        _all = request.GET.get('all', None)

        self.queryset = self.filter_queryset(self.get_queryset())

        # filter by title
        matched = list(filter(lambda r: re.findall(
            title.upper(), r.title.upper()), self.queryset))
        if type:
            matched = list(filter(lambda r: r.type == type, matched))
        if year and year != 0 and year != "":
            matched = list(filter(lambda r: r.year == int(year), matched))

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(matched)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False)
    def statistics(self, request):
        divisions = []
        for div in Division.objects.all():
            divisions.append({
                'name': div.name,
                'value': div.member_set.count()
            })
        return JsonResponse({
            'research': [
              { 'value': self.queryset.filter(type='Article').count(), 'name': 'Articles' },
              { 'value': self.queryset.filter(type='Presentation').count(), 'name': 'Presentations' },
              { 'value': self.queryset.filter(type='Thesis').count(), 'name': 'Theses' },
              { 'value': Project.objects.count(), 'name': 'Projects' }
            ],
            'members': [
              { 'value': Member.objects.filter(active=True).count(), 'name': 'Active' },
              { 'value': Member.objects.filter(active=False).count(), 'name': 'Inactive' }
            ],
            'committee': [
              { 'value': Member.objects.filter(committee=True).count(), 'name': 'Committee' },
              { 'value': Member.objects.filter(board=True).count(), 'name': 'Board' }
            ],
            'divisions': divisions
        })


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
