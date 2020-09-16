from django import forms
from .models import Dairy

class CreateNew(forms.ModelForm):
    class Meta:
        model = Dairy
        fields=['title', 'description']


