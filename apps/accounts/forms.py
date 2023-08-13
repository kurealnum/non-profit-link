from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="Enter your email", max_length=100)
    password = forms.CharField(label="Enter your password", max_length=100)