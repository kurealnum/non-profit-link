from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.accounts.models import Org, OrgContactInfo, OrgInfo, OrgLocation


@login_required
def dashboard(request):
    # getting the current user/org info
    current_user = request.user
    current_org = Org.objects.get(username=current_user.username)
    current_org_location = OrgLocation.objects.get(org=current_org)
    current_org_contact_info = OrgContactInfo.objects.get(org=current_org)
    current_org_info = OrgInfo.objects.get(org=current_org)
    current_org_items = current_org.item_set.all()  # type: ignore not sure why i have to do this, it's a completely valid thingy (whatever you call it)

    print(current_org_items)

    return render(request, "dashboard.html")
