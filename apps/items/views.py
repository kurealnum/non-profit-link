from django.shortcuts import render


def search_items(request):
    return render(request, "search_items.html")


def manage_item_formset(request):
    print("Managaged")
    # TODO
    # check if post or get
    # if post, then validate forms
    if request.method == "POST":
        print("Post")
        pass
        # and do something with the form data to see what's been added, edited, or deleted
        # send some sort of message that says "saved" (can be thru js or django)
