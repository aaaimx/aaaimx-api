from rest_framework import serializers
from .models import *

class AuthorsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {'position': value.position, 'fullname': value.member.fullname, 'active': value.member.active }

class AdvisorListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {'position': value.position, 'fullname': value.member.fullname, 'active': value.member.active }

class ResearchField(serializers.RelatedField):
    def to_representation(self, value):
        return { 'id': value.id, 'title' : value.title }

class AdscriptionField(serializers.RelatedField):
    def to_representation(self, value):
        return value.alias
