from django import forms
from .models import Dairy

class Add_Dairy(forms.ModelForm):
    class Meta:
        model= Dairy
        fields= ['id','title', 'description']