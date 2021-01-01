from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        exclude = []

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = []

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        exclude = []