from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Org, OrgLocation


# basic user change forms
class LoginRegisterForm(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Enter your password", max_length=100
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Org
        fields = ["org_name"]


class CustomUserChangeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Org
        fields = ["org_name"]


# org info form
class OrgLocationEditForm(forms.ModelForm):
    class Meta:
        model = OrgLocation
        fields = "__all__"
