from rest_framework import serializers
from .models import *
from .fields import *

# Serializers define the API representation.


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
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
        fields = [
            "uuid",
            "title",
            "lines",
            "projects",
            "resume",
            "year",
            "grade",
            "event",
            "pub_in",
            "pub_type",
            "type",
            "link",
            "authors",
            "advisors",
        ]


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        exclude = []


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        exclude = []
