from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db.models import Sum, Count, Subquery

from ..accounts.models import Item, Org


def index(request):
    # getting all items, with
    top_5_items = Item.objects.values("org", "item_name", "count").order_by("-count")

    # what we'll send in context
    top_5_items_context = {}

    # getting the top 5 items
    p = 0
    while len(top_5_items_context) < 5 and p < len(top_5_items):
        tmp_item = top_5_items[p]
        # if item does not exist, set it equal to the current value of that
        top_5_items_context[tmp_item["item_name"]] = tmp_item[
            "count"
        ] + top_5_items_context.get(tmp_item["item_name"], 0)

        p += 1

    # getting 5 random models
    total_orgs = Org.objects.count()
    upper_bound = 5 if total_orgs >= 5 else total_orgs
    lower_bound = upper_bound - 5 if upper_bound - 5 >= 0 else 0
    random_5_orgs = Org.objects.all()[lower_bound:upper_bound]

    return render(
        request,
        "home.html",
        context={"random_5_orgs": random_5_orgs, "top_5_items": top_5_items_context},
    )
