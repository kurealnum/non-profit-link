from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.accounts.models import Item, Org, OrgContactInfo, OrgInfo, OrgLocation


@login_required
def dashboard(request):
    # getting the current user/org info
    user = request.user
    org = Org.objects.get(username=user.username)
    org_location = OrgLocation.objects.get(org=org)
    org_contact_info = OrgContactInfo.objects.get(org=org)
    org_info = OrgInfo.objects.get(org=org)
    org_items = Item.objects.filter(org=org)

    return render(
        request,
        "dashboard.html",
        context={
            "org": org,
            "org_location": org_location,
            "org_contact_info": org_contact_info,
            "org_info": org_info,
            "org_items": org_items,
        },
    )


def homepage(request):
    return render(
        request,
        "homepage.html",
    )
