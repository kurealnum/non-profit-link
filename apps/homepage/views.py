from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db.models import Sum, Count, Subquery

from ..accounts.models import Item, Org


def index(request):
    # this only queries for 5 items, per this stackoverflow post: https://stackoverflow.com/questions/6574003/django-limiting-query-results

    top_5_items = []  # just temporary

    # what we'll send in context
    top_5_items_context = []

    for index, item in enumerate(top_5_items):
        # getting and counting all items across all orgs with the same name
        number_of_orgs_with_item = Item.objects.filter(item_name=item)

        # summing those items
        total_count = sum([temp_item.count for temp_item in number_of_orgs_with_item])

        # adding that to what we'll send in context
        top_5_items_context.append([len(number_of_orgs_with_item), total_count])

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
