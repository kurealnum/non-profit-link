from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db.models import Sum, Count, Subquery

from ..accounts.models import Item, Org


def index(request):
    # getting the 5 items with the highest count
    top_5_items = (
        Item.objects.values_list("item_name")
        .annotate(sum=Sum("count"))
        .order_by("-sum")[:5]
    )

    # getting 5 random models
    total_orgs = Org.objects.count()
    upper_bound = 5 if total_orgs >= 5 else total_orgs
    lower_bound = upper_bound - 5 if upper_bound - 5 >= 0 else 0
    random_5_orgs = Org.objects.all()[lower_bound:upper_bound]

    return render(
        request,
        "home.html",
        context={"random_5_orgs": random_5_orgs, "top_5_items": list(top_5_items)},
    )
