from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import Profile

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
