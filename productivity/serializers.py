from rest_framework import serializers
from .models import *
from .fields import *
# Serializers define the API representation.
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = []
        
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = []

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        exclude = []

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        exclude = []

class ResearchSerializer(serializers.ModelSerializer):
    authors = AuthorsListingField(many=True, read_only=True)
    advisors = AdvisorListingField(many=True, read_only=True)
    class Meta:
        model = Research
        exclude = []

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        exclude = []

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = []

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        exclude = []

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        exclude = []

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        exclude = []