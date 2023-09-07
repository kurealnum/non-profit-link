from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import orgs


class LoginRegisterForm(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label="Enter your password", max_length=100)

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        password2 = None
        model = orgs
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
   
    class Meta: 
        password2 = None
        model = orgs
        fields = ("email",)
