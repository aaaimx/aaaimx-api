from rest_framework import serializers
from .models import *


class AuthorsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "position": value.position,
            "id": value.id,
            "member": value.member.id,
            "name": value.member.name,
            "surname": value.member.surname,
            "active": value.member.active,
        }


class AdvisorListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "position": value.position,
            "id": value.id,
            "member": value.member.id,
            "surname": value.member.surname,
            "active": value.member.active,
        }


class ResearchField(serializers.RelatedField):
    def to_representation(self, value):
        return {"uuid": value.uuid, "title": value.title}


class AdscriptionField(serializers.RelatedField):
    def to_representation(self, value):
        return value.alias
