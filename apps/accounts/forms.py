from django import forms


class LoginRegisterForm(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=100)
    password = forms.CharField(label="Enter your password", max_length=100)



