from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Item

API_ERROR_TEMPLATE = "api_error.html"


def search_items(request):
    return render(request, "search_items.html")


@login_required  # type: ignore
def add_item(request, item_name):
    # TODO
    if request.method == "POST":
        print("Post")


def delete_item(request, item_name):
    # TODO
    if request.method == "POST":
        current_user = request.user
        Item.objects.filter(org=current_user, item_name=item_name).delete()
    else:
        return render(request, API_ERROR_TEMPLATE)
