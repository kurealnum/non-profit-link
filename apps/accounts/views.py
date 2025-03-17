from django import forms as forms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import QueryDict, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from .helpers import add_errors_to_password
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
EDIT_ORG_INFO_MODAL = "edit_info_modal.html"
EDIT_ACCOUNT_INFO_MODAL = "edit_account_info_modal.html"
SEARCH_NON_PROFITS_TEMPLATE = "search_non_profits.html"
SEARCH_NON_PROFITS_RESULTS = "search_non_profits_results.html"


@login_required
def edit_org_info(request):
    if request.method == "PUT":
        request_put = QueryDict(request.body)  # type: ignore
        org = request.user.id

        # Get and put data into forms
        existing_contact_form = OrgContactInfo.objects.get(org=org)
        existing_info_form = OrgInfo.objects.get(org=org)
        existing_location_form = OrgLocation.objects.get(org=org)
        contact_form = OrgContactInfoForm(request_put, instance=existing_contact_form)
        info_form = OrgInfoForm(request_put, instance=existing_info_form)
        location_form = OrgLocationForm(request_put, instance=existing_location_form)

        # If all forms are valid, update data and return 201. If not, return 400.
        status = 400
        edit_org_forms = [contact_form, info_form, location_form]
        valid_forms = [form.is_valid() for form in edit_org_forms]

        if all(valid_forms):
            for form in edit_org_forms:
                new_instance = form.save(commit=False)
                new_instance.org = request.user
                new_instance.save()

            status = 201

        return render(
            request,
            EDIT_ORG_INFO_MODAL,
            context={"edit_org_forms": edit_org_forms},
            status=status,
        )

    return HttpResponse(status=405)


@login_required
def edit_account_info(request):
    if request.method == "PUT":
        request_put = QueryDict(request.body)  # type: ignore
        org_form = OrgForm(request_put, instance=request.user)
        status = 400

        # If form is valid, manually validate password. If everything is valid, return 201.
        if org_form.is_valid():
            cleaned_org_form = org_form.cleaned_data
            cur_user = org_form.save(commit=False)

            is_pass_invalid = add_errors_to_password(
                cleaned_org_form["password"], cleaned_org_form["confirm_password"]
            )

            if is_pass_invalid:
                org_form.add_error("password", is_pass_invalid)

            else:
                cur_user.set_password(cleaned_org_form["password"])
                cur_user.save()
                status = 201

        response = render(
            request,
            EDIT_ACCOUNT_INFO_MODAL,
            context={"edit_info_form": org_form},
            status=status,
        )

        # See HTMX docs for more information on this header: https://htmx.org/headers/hx-redirect/
        if status == 201:
            response["HX-Redirect"] = reverse("login")

        return response

    return HttpResponse(status=405)


def login_user(request):
    login_register_form = LoginRegisterForm()

    if request.method == "POST":
        login_register_form = LoginRegisterForm(request.POST)

        # If the form is valid, try and authenticate. If authentication fails, do not redirect to dashboard.
        if login_register_form.is_valid():
            login_register = login_register_form.cleaned_data

            # inputted data
            username = login_register["username"]
            password = login_register["password"]

            try:
                user = authenticate(username=username, password=password)
            except (
                ValidationError
            ) as e:  # ValidationError is raised from backends.py. This is done to see which of the credentials is invalid
                if e.message == "Invalid Username":
                    login_register_form.add_error("username", e.message)
                else:
                    login_register_form.add_error("password", e.message)

            else:
                login(request, user)

                return redirect("dashboard")

    return render(request, LOGIN_FORM, {"form": login_register_form})


def register_user(request):
    # If request.POST is none, then the user is GETing the page.
    user_info_form = OrgForm(request.POST or None)
    input_forms = [
        OrgLocationForm(request.POST or None),
        OrgContactInfoForm(request.POST or None),
        OrgInfoForm(request.POST or None),
    ]

    if request.method == "POST" and user_info_form.is_valid():
        validated_forms_count = [form.is_valid() for form in input_forms]
        cleaned_user_info_form = user_info_form.cleaned_data

        is_pass_invalid = add_errors_to_password(
            cleaned_user_info_form["password"],
            cleaned_user_info_form["confirm_password"],
        )

        if is_pass_invalid:
            user_info_form.add_error("password", is_pass_invalid)

        if all(validated_forms_count) and not is_pass_invalid:
            new_user = user_info_form.save(commit=False)
            new_user.set_password(cleaned_user_info_form["password"])
            new_user.save()

            # Save all data if it is valid
            for form in input_forms:
                newform = form.save(commit=False)
                newform.org = new_user
                newform.save()

            messages.add_message(
                request, messages.SUCCESS, "You have been successfully registered!"
            )
            return redirect(reverse("login"))

    return render(
        request,
        REGISTER_FORM,
        {"forms": [user_info_form] + input_forms},
    )


def search_non_profits(request):
    if not request.POST:
        orgs = Org.objects.all().select_related("orglocation")
        return render(request, SEARCH_NON_PROFITS_TEMPLATE, context={"orgs": orgs})

    is_org = request.POST.get("org")
    search = request.POST.get("search")
    # either country, region, zipcode, city, or street-address
    location_options = request.POST.get("location-options")

    orgs = None

    if is_org == "org":
        orgs = Org.objects.filter(username__trigram_similar=search).select_related(
            "orglocation"
        )

    if is_org == "location":
        orgs = Org.objects.all().select_related("orglocation")
        match location_options:
            case "country":
                orgs = orgs.filter(orglocation__country__trigram_similar=search)
            case "region":
                orgs = orgs.filter(orglocation__region__trigram_similar=search)
            case "city":
                orgs = orgs.filter(orglocation__city__trigram_similar=search)
            case "zipcode":
                orgs = orgs.filter(orglocation__zip__contains=search)
            case "street-address":
                orgs = orgs.filter(orglocation__street_address__trigram_similar=search)

    return render(
        request,
        SEARCH_NON_PROFITS_RESULTS,
        context={
            "orgs": orgs,
            "search": search,
            "org": is_org,
            "location_options": location_options,
        },
    )
