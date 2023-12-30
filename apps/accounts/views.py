from django import forms as forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Org, OrgContactInfo, OrgInfo, OrgLocation

from .forms import (
    LoginRegisterForm,
    OrgContactInfoForm,
    OrgForm,
    OrgInfoForm,
    OrgLocationForm,
)

LOGIN_FORM = "login.html"
REGISTER_FORM = "register.html"


class EditAccountApiView(APIView):
    def put(self, request):
        data = request.data
        user = request.user
        org = Org.objects.get(username=user.username)
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        # if password, update password
        if password and confirm_password:
            Org.objects.filter(username=user.username).update_or_create(
                password=password
            )

        # update rest of data
        Org.objects.update_or_create(
            username=user.username, defaults={"username": data.get("username")}
        )
        OrgContactInfo.objects.update_or_create(
            org=org, defaults={"phone": data.get("phone"), "email": data.get("email")}
        )
        OrgInfo.objects.update_or_create(
            org=org, defaults={"desc": data.get("desc"), "website": data.get("website")}
        )
        OrgLocation.objects.update_or_create(
            org=org,
            defaults={
                "country": data.get("country"),
                "region": data.get("region"),
                "zip": data.get("zip"),
                "city": data.get("city"),
                "street_address": data.get("street_address"),
            },
        )

        return Response(status=status.HTTP_200_OK)


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
