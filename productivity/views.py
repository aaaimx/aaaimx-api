from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse

from django.db.models import Q, Sum
from .serializers import *
from .models import *
from logistic.models import Certificate
from finances.models import Invoice
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
        division = request.GET.get('division', None)
        _all = request.GET.get('all', None)
        order = request.GET.get('order', '-charge')

        if panel == "true":
            self.queryset = Member.objects.filter(Q(name__icontains=name) | Q(
                surname__icontains=name), Q(committee=True) | Q(board=True)).order_by(order)
        elif division:
            self.queryset = Member.objects.filter(
                Q(name__icontains=name) | Q(surname__icontains=name), divisions__name=division).order_by(order)
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

    @action(detail=True, methods=['GET'])
    def research(self, request, pk=None):
        authorship = Author.objects.filter(member=pk)
        advisory = Author.objects.filter(member=pk)
        leaders = Member.objects.get(id=pk).project_set.all()
        data = [author.research for author in authorship.union(advisory)]
        research = ResearchSerializer(data, many=True)
        projects = ProjectSerializer(leaders, many=True)
        return Response({
            'projects': projects.data,
            'research': research.data
        })

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

    @action(detail=False, methods=['get'])
    def panel(self, request):
        panel_members = Member.objects.filter(Q(committee=True) | Q(board=True)
                                              ).order_by('-name')
        serializer = self.get_serializer(panel_members, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def divisions(self, request):
        division_members = Member.objects.all().order_by('-name')
        division_members = list(
            filter(lambda m: m.divisions.all() or m.board, division_members))
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
    
    @action(detail=True, methods=['GET'])
    def research(self, request, pk=None):
        data = Project.objects.filter(institute=pk)
        members = Member.objects.filter(adscription=pk)
        research = []
        for proj in data:
            research += proj.research_set.all()
        projects = ProjectSerializer(data, many=True)
        research = ResearchSerializer(research, many=True)
        members = MemberSerializer(members, many=True)
        return Response({
            'projects': projects.data,
            'research': research.data,
            'members': members.data,
        })


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

    @action(detail=True, methods=['GET'])
    def research(self, request, pk=None):
        projects = Line.objects.get(pk=pk).project_set.all()
        research = Line.objects.get(pk=pk).research_set.all()
        projects = ProjectSerializer(projects, many=True)
        research = ResearchSerializer(research, many=True)
        return Response({
            'projects': projects.data,
            'research': research.data
        })


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
        line = request.GET.get('line', None)
        _all = request.GET.get('all', None)

        self.queryset = Project.objects.filter(
            title__icontains=title).order_by('title')

        if line:
            self.queryset = self.queryset.filter(lines=line)

        if institute:
            self.queryset = self.queryset.filter(institute__alias=institute)

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(self.queryset)
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
        type = request.GET.get('type', "")
        line = request.GET.get('line', None)
        _all = request.GET.get('all', None)

        self.queryset = Research.objects.filter(
            title__icontains=title, type__icontains=type).order_by('-year')

        if line:
            self.queryset = self.queryset.filter(lines=line)

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        divisions = []
        for div in Division.objects.all():
            divisions.append({
                'name': div.name,
                'value': div.member_set.count()
            })
        return JsonResponse({
            'research': [
                {'value': self.queryset.filter(
                    type='Article').count(), 'name': 'Articles'},
                {'value': self.queryset.filter(
                    type='Presentation').count(), 'name': 'Presentations'},
                {'value': self.queryset.filter(
                    type='Thesis').count(), 'name': 'Theses'},
                {'value': Project.objects.count(), 'name': 'Projects'}
            ],
            'certs': [
                {'value': Certificate.objects.filter(
                    type='PARTICIPATION').count(), 'name': 'PARTICIPATION'},
                {'value': Certificate.objects.filter(
                    type='RECOGNITION').count(), 'name': 'RECOGNITION'},
                {'value': Certificate.objects.filter(
                    type='APPRECIATION').count(), 'name': 'APPRECIATION'}
            ],
            'partners': [
                {'value': Partner.objects.filter(
                    type='Sponsor').count(), 'name': 'Sponsors'},
                {'value': Partner.objects.filter(
                    type='Research Center').count(), 'name': 'Research Centers'},
                {'value': Partner.objects.filter(
                    type='Division').count(), 'name': 'Divisions'},
                {'value': Partner.objects.filter(
                    type='Partner').count(), 'name': 'Partners'}
            ],
            'members': [
                {'value': Member.objects.filter(
                    active=True).count(), 'name': 'Active'},
                {'value': Member.objects.filter(
                    active=False).count(), 'name': 'Inactive'}
            ],
            'committee': [
                {'value': Member.objects.filter(
                    committee=True).count(), 'name': 'Committee'},
                {'value': Member.objects.filter(
                    board=True).count(), 'name': 'Board'}
            ],
            'finances': [
                {'value': Invoice.objects.filter(type='Income').aggregate(
                    Sum('amount')).get('amount__sum', 0), 'name': 'Incomes'},
                {'value': Invoice.objects.filter(type='Donation').aggregate(
                    Sum('amount')).get('amount__sum', 0), 'name': 'Donation'},
                {'value': Invoice.objects.filter(type='Expense').aggregate(
                    Sum('amount')).get('amount__sum', 0), 'name': 'Expenses'}
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
