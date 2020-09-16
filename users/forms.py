from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class create_user(UserCreationForm):
    contact = forms.CharField(max_length=11, required=True)
    address = forms.CharField(max_length=300, required=False)
    class Meta:
        model=User
        fields= ['username', 'email', 'contact', 'address','password1', 'password2']