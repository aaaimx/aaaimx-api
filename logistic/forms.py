# django forms
from django import forms
from .models import Certificate

class CertFile(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('file',)