from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def login_user(request):
    template = loader.get_template('login.html')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["email"])

    #else is a GET request
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
