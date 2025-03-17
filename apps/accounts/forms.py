from django import forms
from django.utils.safestring import mark_safe

from .models import Org, OrgContactInfo, OrgInfo, OrgLocation
from apps.items.models import Item


# Authentication forms
class LoginRegisterForm(forms.Form):
    username = forms.CharField(label="Enter your organizations name", max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Enter your password", max_length=100
    )


class OrgForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=mark_safe(
            'Password:<ul id="password-specification"><li>Must be 8 characters or longer</li><li>Must use a special character/number</li><li>Must not be similar to your organizations name</li></ul>'
        ),
    )
    password.label_suffix = ""
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Org
        fields = ["username"]


# Forms for Org information
class OrgLocationForm(forms.ModelForm):
    class Meta:
        model = OrgLocation
        fields = "__all__"
        widgets = {"org": forms.HiddenInput()}


class OrgContactInfoForm(forms.ModelForm):
    class Meta:
        model = OrgContactInfo
        fields = "__all__"
        widgets = {"org": forms.HiddenInput()}


class OrgInfoForm(forms.ModelForm):
    class Meta:
        model = OrgInfo
        fields = "__all__"
        widgets = {"org": forms.HiddenInput()}


# Form for item
class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {"org": forms.HiddenInput()}
