from django.shortcuts import render


def search_items(request):
    return render(request, "search_items.html")


def add_item(request, item_name):
    # TODO
    if request.method == "POST":
        print("Post")


def delete_item(request, item_name):
    # TODO
    if request.method == "POST":
        print("Post")
