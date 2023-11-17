from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from ..accounts.models import Item, Org


def index(request):
    # this only queries for 5 items, per this stackoverflow post: https://stackoverflow.com/questions/6574003/django-limiting-query-results
    top_5_items = Item.objects.all().order_by("-count")[:5]

    # getting 5 random models
    total_orgs = Org.objects.count()
    upper_bound = 5 if total_orgs >= 5 else total_orgs
    lower_bound = upper_bound - 5 if upper_bound - 5 >= 0 else 0
    random_5_orgs = Org.objects.all()[lower_bound:upper_bound]

    return render(
        request,
        "home.html",
        context={"random_5_orgs": random_5_orgs, "top_5_items": top_5_items},
    )
