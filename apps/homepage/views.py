from django.db.models import Count, Subquery, Sum, OuterRef
from django.shortcuts import render

from ..accounts.models import Item, Org, OrgLocation


def index(request):
    # getting the 5 items with the highest count, and the number of orgs that need that item
    top_5_items = (
        Item.objects.values_list("item_name")
        .annotate(sum=Sum("count"), org_count=Count("org"))
        .order_by("-sum")[:5]
    )

    # query for 5 semi-random
    random_5_orgs = (
        Org.objects.select_related("orglocation")
        .values_list("username", "orglocation__region", "orglocation__city")
        .order_by("?")[:5]
    )

    return render(
        request,
        "home.html",
        context={
            "random_5_orgs": list(random_5_orgs),
            "top_5_items": list(top_5_items),
            # "random_5_orgs_location": list(random_5_orgs_location),
        },
    )
