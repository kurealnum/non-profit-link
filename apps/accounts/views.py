from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import (
    CustomUserCreationForm,
    LoginRegisterForm,
    OrgLocationEditForm,
    OrgContactInfoEditForm,
    OrgInfoEditForm,
)
from .managers import CustomUserManager
from .models import Org

LOGIN_FORM = "login.html"
REGISTER_FORM = "register.html"

CUserManager = CustomUserManager()


def login_user(request):
    if request.method == "POST":
        form = LoginRegisterForm(request.POST)

        # if the form isn't empty
        if form.is_valid():
            # data
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)

            # if authenticate returns a user object, which means that the user is valid
            if user:
                login(request, user)

                return redirect("dashboard")

            # else error with the form (add more to this later)
            else:
                messages.error(request, "Incorrect email and/or password")
                return redirect("login")

    # else is a GET request
    else:
        form = LoginRegisterForm()

        return render(request, LOGIN_FORM, {"form": form})


def logout_user(request):
    # super simple view :)
    logout(request)

    return redirect("/")


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        # if the form isn't empty
        if form.is_valid():
            # data
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            # create user
            Org.objects.create_user(name=email, password=password)

            return redirect("/accounts/login")

        # else error with the form (add more to this later)
        else:
            messages.error(
                request,
                "Please enter a more secure password and ensure that your passwords are the same length",
            )
            return redirect("register")

    # else a get request
    else:
        org = CustomUserCreationForm()
        locations_form = OrgLocationEditForm()
        contact_form = OrgContactInfoEditForm()
        general_info_form = OrgInfoEditForm()

        return render(
            request,
            REGISTER_FORM,
            {
                "org": org,
                "locations_form": locations_form,
                "contact_form": contact_form,
                "general_info_form": general_info_form,
            },
        )
