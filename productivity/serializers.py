from rest_framework import serializers
from .models import Member, Research

# Serializers define the API representation.
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = []

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        exclude = []
        