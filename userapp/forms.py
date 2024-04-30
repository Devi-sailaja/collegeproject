from django import forms
from .models import Farmstore
from django.contrib.auth.models import User

class FarmstoreForm(forms.ModelForm):
    class Meta:
        model = Farmstore
        fields = ['name', 'type','cost','mdate',]
    
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password',]

