from django.shortcuts import render


# Create your views here.
def search_items(request):
    return render(request, "search_items.html")
