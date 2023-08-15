from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginRegisterForm, CustomUserCreationForm
from .models import CustomUser
from .managers import CustomUserManager

LOGIN_FORM = "login.html"
REGISTER_FORM = "register.html"

CUserManager = CustomUserManager()


def login_user(request):

    if request.method == "POST":
        form = LoginRegisterForm(request.POST)

        #if the form isn't empty
        if form.is_valid():

            #data
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            
            #if authenticate returns a user object, which means that the user is valid
            if user:
                login(request, user)

                return redirect('/')
            
            else:
                return HttpResponse("You need to fix this form")

    #else is a GET request
    else:
        form = LoginRegisterForm()

        return render(request, LOGIN_FORM, {"form": form})


def logout_user(request):
    logout(request)

    return redirect('/')


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        #if the form isn't empty
        if form.is_valid():

            #data
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            CustomUser.objects.create_user(email=email, password=password)

            return redirect('/accounts/login')

        else:
            return HttpResponse("You need to fix this form")
    
    else:
        form = CustomUserCreationForm()

        return render(request, REGISTER_FORM, {"form": form})