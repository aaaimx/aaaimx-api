from django import forms
from .models import Membership

class MemFile(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('file',)