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
from .helpers import create_big_form
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
    if request.method == "POST":
        data = request.POST

        # still need to figure out how to get the post data into these forms
        forms = [
            CustomUserCreationForm(data),
            OrgLocationEditForm(data),
            OrgContactInfoEditForm(data),
            OrgInfoEditForm(data),
        ]

        # validating forms
        validated_forms_count = [form.is_valid() for form in forms]

        # if all of the forms are valid
        if sum(validated_forms_count) == len(forms):
            new_user = forms[0].save()

            # TODO: save forms
            for form in forms[1:]:
                newform = form.save(commit=False)
                newform.org = new_user
                newform.save()

            return redirect("/accounts/login/")

        # else error with the form
        else:
            user_forms = [
                CustomUserCreationForm(data),
                OrgLocationEditForm(data),
                OrgContactInfoEditForm(data),
                OrgInfoEditForm(data),
            ]

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
