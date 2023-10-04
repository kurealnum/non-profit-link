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
        login_register = LoginRegisterForm(request.POST)

        # if the form isn't empty
        if login_register.is_valid():
            login_register = login_register.cleaned_data

            # data
            email = login_register["email"]
            password = login_register["password"]
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
        data = request.POST
        org = CustomUserCreationForm(data)
        locations_form = OrgLocationEditForm(data)
        contact_form = OrgContactInfoEditForm(data)
        general_info_form = OrgInfoEditForm(data)

        valid_forms_count = [
            org.is_valid(),
            locations_form.is_valid(),
            contact_form.is_valid(),
            general_info_form.is_valid(),
        ]

        # if the forms are valid
        if sum(valid_forms_count) == len(valid_forms_count):
            # cleaning data
            org = org.cleaned_data
            locations_form = locations_form.cleaned_data
            contact_form = contact_form.cleaned_data
            general_info_form = general_info_form.cleaned_data

            # create user
            org = Org.objects.create_user(
                name=org["org_name"], password=org["password"]
            )

            # just for testing right now
            org.country = locations_form["country"]
            org.save()

            return redirect("/accounts/login/")

        # else error with the form (add more to this later)
        else:
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
