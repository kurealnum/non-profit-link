from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.accounts.models import Org, OrgContactInfo, OrgInfo, OrgLocation


@login_required
def dashboard(request):
    # getting the current user/org info
    user = request.user
    org = Org.objects.get(username=user.username)
    org_location = OrgLocation.objects.get(org=org)
    org_contact_info = OrgContactInfo.objects.get(org=org)
    org_info = OrgInfo.objects.get(org=org)
    wanted_org_items = org.item_set.filter(want=True)  # type: ignore
    needed_org_items = org.item_set.filter(want=False)  # type: ignore not sure why i have to do this, it's a completely valid thingy (whatever you call it)

    return render(
        request,
        "dashboard.html",
        context={
            "org": org,
            "org_location": org_location,
            "org_contact_info": org_contact_info,
            "org_info": org_info,
            "wanted_org_items": wanted_org_items,
            "needed_org_items": needed_org_items,
        },
    )
