from django import forms

from .models import Org, OrgLocation, OrgContactInfo, OrgInfo, Item


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


# org info forms
class OrgLocationEditForm(forms.ModelForm):
    class Meta:
        model = OrgLocation
        fields = "__all__"
        exclude = ("org",)


class OrgContactInfoEditForm(forms.ModelForm):
    class Meta:
        model = OrgContactInfo
        fields = "__all__"
        exclude = ("org",)


class OrgInfoEditForm(forms.ModelForm):
    class Meta:
        model = OrgInfo
        fields = "__all__"
        exclude = ("org",)


# item form
class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        exclude = ("org",)
