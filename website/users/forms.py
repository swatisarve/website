from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=101)
    last_name=forms.CharField(max_length=101)
    email=forms.EmailField()
    mobileno=forms.CharField(max_length=101)
    area=forms.CharField(max_length=101)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','mobileno','area','password1','password2']
