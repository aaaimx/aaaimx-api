from rest_framework import serializers
from .models import *
from .fields import *

# Serializers define the API representation.


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = []


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        exclude = []
