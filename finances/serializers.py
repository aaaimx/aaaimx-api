from rest_framework import serializers
from .models import *

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        exclude = []