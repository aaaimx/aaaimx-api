from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = []
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = []

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        exclude = []

class ThesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thesis
        exclude = []


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = []


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
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