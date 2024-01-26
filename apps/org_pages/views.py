from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.accounts.models import Org, OrgContactInfo, OrgInfo, OrgLocation
from apps.accounts.forms import (
    OrgForm,
    OrgContactInfoForm,
    OrgInfoForm,
    OrgLocationForm,
)
from apps.items.models import Item


@login_required  # type: ignore
def dashboard(request):
    # getting the current user/org info
    user = request.user
    username = user.username
    org = Org.objects.get(username=username)
    wanted_org_items = Item.objects.filter(org=org, want=True)
    surplus_org_items = Item.objects.filter(org=org, want=False)

    org_form_initial_data = {"username": username}

    contact_form_initial_data = (
        OrgContactInfo.objects.filter(org=org).values("email", "phone").first()
    )

    info_form_initial_data = (
        OrgInfo.objects.filter(org=org).values("desc", "website").first()
    )

    location_form_initial_data = (
        OrgLocation.objects.filter(org=org)
        .values("country", "region", "zip", "city", "street_address")
        .first()
    )

    # adding the default values
    edit_org_forms = [
        OrgContactInfoForm(initial=contact_form_initial_data),
        OrgInfoForm(initial=info_form_initial_data),
        OrgLocationForm(initial=location_form_initial_data),
    ]

    # if get, just return 2 new forms
    return render(
        request,
        "dashboard.html",
        context={
            "org": org,
            "wanted_org_items": wanted_org_items,
            "surplus_org_items": surplus_org_items,
            "edit_org_forms": edit_org_forms,
            "edit_info_form": OrgForm(initial=org_form_initial_data),
        },
    )


def homepage(request, org_name):
    # getting the current user/org info
    if not Org.objects.filter(username=org_name).exists():
        return redirect("org_does_not_exist")

    org = Org.objects.get(username=org_name)
    org_location = OrgLocation.objects.get(org=org)
    org_contact_info = OrgContactInfo.objects.get(org=org)
    org_info = OrgInfo.objects.get(org=org)
    wanted_org_items = Item.objects.filter(org=org, want=True)
    shared_org_items = Item.objects.filter(org=org, want=False)

    return render(
        request,
        "homepage.html",
        context={
            "org": org,
            "org_location": org_location,
            "org_contact_info": org_contact_info,
            "org_info": org_info,
            "wanted_org_items": wanted_org_items,
            "shared_org_items": shared_org_items,
        },
    )


def org_does_not_exist(request):
    return render(request, "org_does_not_exist.html")
