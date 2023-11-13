from django import forms
from django.utils.safestring import mark_safe

from .models import Item, Org, OrgContactInfo, OrgInfo, OrgLocation


# basic user change forms
class LoginRegisterForm(forms.Form):
    username = forms.CharField(label="Enter your organizations name", max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Enter your password", max_length=100
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=mark_safe(
            "Your password must:<br />-Be longer than 8 characters<br />-Have an uppercase and lowercase characters<br />-Use a special character/number"
        ),
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Org
        fields = ["username"]


class CustomUserChangeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Org
        fields = ["username"]


# org info forms
class OrgLocationEditForm(forms.ModelForm):
    class Meta:
        model = OrgLocation
        fields = "__all__"
        widgets = {"org": forms.HiddenInput()}


class OrgContactInfoEditForm(forms.ModelForm):
    class Meta:
        model = OrgContactInfo
        fields = "__all__"
        widgets = {"org": forms.HiddenInput()}


class OrgInfoEditForm(forms.ModelForm):
    class Meta:
        model = OrgInfo
        fields = "__all__"
        widgets = {"org": forms.HiddenInput()}


# item form
class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {"org": forms.HiddenInput()}
