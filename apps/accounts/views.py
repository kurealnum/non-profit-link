from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.password_validation import validate_password
from django import forms as forms
from django.forms import ValidationError

from .forms import (
    CustomUserCreationForm,
    LoginRegisterForm,
    OrgContactInfoEditForm,
    OrgInfoEditForm,
    OrgLocationEditForm,
)

from .managers import CustomUserManager
from .models import Org

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
    user_info_form = CustomUserCreationForm(request.POST or None)

    # init the forms
    input_forms = [
        OrgLocationEditForm(request.POST or None),
        OrgContactInfoEditForm(request.POST or None),
        OrgInfoEditForm(request.POST or None),
    ]

    # if the user submitted, they're trying to register, so do register stuff:
    if request.method == "POST" and user_info_form.is_valid():
        # validating forms
        validated_forms_count = [form.is_valid() for form in input_forms]

        for i in input_forms:
            print(i.errors)

        # check if password is valid
        cleaned_user_info_form = user_info_form.cleaned_data

        # attempt to validate the password
        try:
            validate_password(cleaned_user_info_form["password"])
        except ValidationError:
            user_info_form.add_error(
                "password", "Your password does not meet the requirements!"
            )
            return render(
                request,
                REGISTER_FORM,
                {"forms": [user_info_form] + input_forms},
            )

        # check if password = password2
        if (
            cleaned_user_info_form["password"]
            != cleaned_user_info_form["confirm_password"]
        ):
            user_info_form.add_error("password", "Your passwords do not match!")
            return render(
                request,
                REGISTER_FORM,
                {"forms": [user_info_form] + input_forms},
            )

        if all(validated_forms_count):
            # inital save on the new user
            new_user = user_info_form.save(commit=False)
            new_user.set_password(cleaned_user_info_form["password"])
            new_user.save()

            # save forms
            for form in input_forms:
                newform = form.save(commit=False)
                newform.org = new_user
                newform.save()

            return redirect("/accounts/login/")

    return render(
        request,
        REGISTER_FORM,
        {"forms": [user_info_form] + input_forms},
    )
