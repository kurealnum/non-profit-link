from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.accounts.models import Org, OrgContactInfo, OrgInfo, OrgLocation
from apps.items.models import Item
from apps.items.forms import CustomItemForm


@login_required  # type: ignore
def dashboard(request):
    # getting the current user/org info
    user = request.user
    org = Org.objects.get(username=user.username)
    org_location = OrgLocation.objects.get(org=org)
    org_contact_info = OrgContactInfo.objects.get(org=org)
    org_info = OrgInfo.objects.get(org=org)
    wanted_org_items = Item.objects.filter(org=org, want=True)
    surplus_org_items = Item.objects.filter(org=org, want=False)

    # TODO
    # check if post or get
    # if post, then validate forms
    if request.method == "POST":
        pass
        # and do something with the form data to see what's been added, edited, or deleted
        # send some sort of message that says "saved" (can be thru js or django)

    # if get, just return 2 new forms
    if request.method == "GET":
        needed_items_form = CustomItemForm()
        return render(
            request,
            "dashboard.html",
            context={
                "org": org,
                "org_location": org_location,
                "org_contact_info": org_contact_info,
                "org_info": org_info,
                "wanted_org_items": wanted_org_items,
                "surplus_org_items": surplus_org_items,
                "needed_items_form": needed_items_form,
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
    org_items = Item.objects.filter(org=org)

    return render(
        request,
        "homepage.html",
        context={
            "org": org,
            "org_location": org_location,
            "org_contact_info": org_contact_info,
            "org_info": org_info,
            "org_items": org_items,
        },
    )


def org_does_not_exist(request):
    return render(request, "org_does_not_exist.html")
