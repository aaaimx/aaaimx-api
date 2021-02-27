from rest_framework import serializers
from .models import *

# Serializers define the API representation.


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        exclude = []


class CertificateSerializerDeep(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        exclude = []
        depth = 1


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        exclude = []


class ParticipantSerializerDeep(serializers.ModelSerializer):
    class Meta:
        model = Participant
        exclude = []
        depth = 1


class EventSerializer(serializers.ModelSerializer):
    corum = serializers.IntegerField(required=False, default=0)

    class Meta:
        model = Event
        exclude = []


class EventSerializerDeep(serializers.ModelSerializer):
    
    participants = ParticipantSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Event
        exclude = []
        depth = 1
