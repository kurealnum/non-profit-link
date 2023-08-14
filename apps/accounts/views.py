from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def login_user(request):
    print(request)

    if request.method == "POST":
        form = LoginForm(request.POST)

        #if the form isn't empty
        if form.is_valid():

            #data
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            
            #if authenticate returns a user object, which means that the user is valid
            if user:
                login(request, user)

    #else is a GET request
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_user(request):
    pass
