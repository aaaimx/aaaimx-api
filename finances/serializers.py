from rest_framework import serializers
from .models import *

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        exclude = []

class BankMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankMovement
        exclude = []