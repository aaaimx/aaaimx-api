from rest_framework import serializers
from .models import *

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        exclude = []

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        exclude = []