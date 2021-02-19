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
                Q(name__icontains=name) | Q(surname__icontains=name), divisions__icontains=division).order_by(order)
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

