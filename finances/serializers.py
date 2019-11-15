from rest_framework import serializers
from .models import Membership

# Serializers define the API representation.
class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        exclude = []