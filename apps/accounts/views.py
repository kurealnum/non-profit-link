from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import (
    CustomUserCreationForm,
    LoginRegisterForm,
    OrgContactInfoEditForm,
    OrgInfoEditForm,
    OrgLocationEditForm,
)
from .managers import CustomUserManager
from .models import Org
from .helpers import create_big_form

LOGIN_FORM = "login.html"
REGISTER_FORM = "register.html"

CUserManager = CustomUserManager()


def login_user(request):
    if request.method == "POST":
        login_register_form = LoginRegisterForm(request.POST)

        # if the form isn't empty
        if login_register_form.is_valid():
            login_register = login_register_form.cleaned_data

            # data
            org_name = login_register["org_name"]
            password = login_register["password"]
            user = authenticate(request, org_name=org_name, password=password)

            # if authenticate returns a user object, which means that the user is valid
            if user:
                login(request, user)

                return redirect("dashboard")

            # else error with the form (add more to this later)
            else:
                return render(request, LOGIN_FORM, {"form": login_register_form})

    # else is a GET request
    else:
        login_register_form = LoginRegisterForm()

        return render(request, LOGIN_FORM, {"form": login_register_form})


def logout_user(request):
    # super simple view :)
    logout(request)

    return redirect("/")


def register_user(request):
    if request.method == "POST":
        data = request.POST

        # still need to figure out how to get the post data into these forms
        user_forms = create_big_form(
            CustomUserCreationForm(data),
            OrgLocationEditForm(data),
            OrgContactInfoEditForm(data),
            OrgInfoEditForm(data),
        )

        valid_forms_count = [form.is_valid() for form in user_forms]

        # if the forms are valid
        if sum(valid_forms_count) == len(valid_forms_count):
            # cleaning data
            user_forms = [form.cleaned_data for form in user_forms]

            # create user
            org = Org.objects.create_user(
                name=user_forms[0]["org_name"], password=user_forms[0]["password"]
            )

            # just for testing right now
            org.country = user_forms[1]["country"]
            org.save()

            return redirect("/accounts/login/")

        # else error with the form (add more to this later)
        else:
            return render(
                request,
                REGISTER_FORM,
                {
                    "forms": user_forms,
                },
            )

    # else a get request
    else:
        # org = CustomUserCreationForm()
        # locations_form = OrgLocationEditForm()
        # contact_form = OrgContactInfoEditForm()
        # general_info_form = OrgInfoEditForm()

        forms = create_big_form(
            None,
            CustomUserCreationForm(),
            OrgLocationEditForm(),
            OrgContactInfoEditForm(),
            OrgInfoEditForm(),
        )

        return render(
            request,
            REGISTER_FORM,
            {"forms": forms},
        )
