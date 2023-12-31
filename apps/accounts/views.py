from django.http import QueryDict
from django import forms as forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.shortcuts import redirect, render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Org, OrgContactInfo, OrgInfo, OrgLocation

from .serializers import (
    OrgContactInfoSerializer,
    OrgInfoSerializer,
    OrgLocationSerializer,
)

from .forms import (
    LoginRegisterForm,
    OrgContactInfoForm,
    OrgForm,
    OrgInfoForm,
    OrgLocationForm,
)

LOGIN_FORM = "login.html"
REGISTER_FORM = "register.html"


@login_required  # type: ignore
def edit_org_info(request):
    if request.method == "PUT":
        request_put = QueryDict(request.body)

        contact_form = OrgContactInfoForm(request_put, instance=request.user)
        info_form = OrgInfoForm(request_put, instance=request.user)
        location_form = OrgLocationForm(request_put, instance=request.user)
        edit_org_forms = [contact_form, info_form, location_form]
        status = 400

        if (
            contact_form.is_valid()
            and info_form.is_valid()
            and location_form.is_valid()
        ):
            contact_form.save()
            info_form.save()
            location_form.save()
            status = 201

        return render(
            request,
            "edit_info_modal.html",
            context={"edit_org_forms": edit_org_forms},
            status=status,
        )


@login_required  # type: ignore
def edit_account_info(request):
    if request.method == "PUT":
        request_put = QueryDict(request.body)
        org_form = OrgForm(request_put, instance=request.user)
        status = 400

        if org_form.is_valid():
            # do this so we can have custom password field in OrgForm
            cleaned_org_form = org_form.cleaned_data
            cur_user = org_form.save(commit=False)
            password = cleaned_org_form["password"]
            confirm_password = cleaned_org_form["confirm_password"]
            try:
                validate_password(password)
            except ValidationError:
                org_form.add_error(
                    "password", "Your password does not meet the requirements!"
                )
            if password != confirm_password:
                org_form.add_error("password", "Your passwords do not match!")

            if not org_form.errors:
                cur_user.set_password(cleaned_org_form["password"])
                cur_user.save()
                status = 201

        response = render(
            request,
            "edit_account_info_modal.html",
            context={"edit_info_form": org_form},
            status=status,
        )

        if status == 201:
            response["HX-Redirect"] = "/accounts/login/"

        return response


def login_user(request):
    if request.method == "POST":
        login_register_form = LoginRegisterForm(request.POST)

        # essentially just checking if the form isn't empty
        if login_register_form.is_valid():
            login_register = login_register_form.cleaned_data

            # inputted data
            username = login_register["username"]
            password = login_register["password"]
            user = authenticate(request, username=username, password=password)

            # if authenticate returns a user object, the user is valid
            if user:
                login(request, user)

                return redirect("dashboard")

            # else error with the form
            else:
                login_register_form.add_error(None, "Username or password is incorrect")
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
    user_info_form = OrgForm(request.POST or None)

    # init the forms
    input_forms = [
        OrgLocationForm(request.POST or None),
        OrgContactInfoForm(request.POST or None),
        OrgInfoForm(request.POST or None),
    ]

    # if the user submitted the form and the form is valid
    if request.method == "POST" and user_info_form.is_valid():
        # validating forms
        validated_forms_count = [form.is_valid() for form in input_forms]

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

        # check if password = confirm password
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


def search_non_profits(request):
    return render(request, "non_profits.html")
