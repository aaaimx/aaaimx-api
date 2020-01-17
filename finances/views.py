

from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import viewsets
from .forms import MemFile
from utils.images import generate_membership, LOCATION


# Create your views here.
class MembershipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Memberships to be viewed or edited.
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def list(self, request):
        """
        GET method to process pagination, filtering & sort
        """
        # get query params
        to = request.GET.get('to', "")
        query = request.GET.get('query', "")
        type = request.GET.get('type', "")
        status = request.GET.get('status', None)
        _all = request.GET.get('all', None)

        self.queryset = self.queryset.filter(Q(to__icontains=to))
        if query:
            self.queryset = self.queryset.filter(description__icontains=query)
        if type:
            self.queryset = self.queryset.filter(type=type)

        # filter by status
        if status:
            self.queryset = self.queryset.filter(published=status.capitalize())

        # serialize data
        if _all is not None:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)

        # pagination
        page = self.paginate_queryset(self.queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def generate_mem(self, serializer, avatar):
        uuid = serializer.data['uuid']
        name = serializer.data['display_name']
        url = 'http://www.aaaimx.org/memberships/?id={0}'.format(uuid)
        imgMembership = generate_membership(name, uuid, url, avatar)
        inst = Membership.objects.filter(pk=uuid).update(QR=url)
        inst = Membership.objects.get(pk=uuid)
        m = MemFile(files={'file': imgMembership }, instance=inst)
        if m.is_valid():
            m.save(commit=False)
            m.save()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.generate_mem(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Membership.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        avatar = request.FILES.get('file', None)
        if avatar:
            print(dir(avatar))
            self.generate_mem(serializer, avatar)
            
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class BankMovementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BankMovements to be viewed or edited.
    """
    queryset = BankMovement.objects.all()
    serializer_class = MembershipSerializer