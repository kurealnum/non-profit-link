from django.urls import path

from . import views

urlpatterns = [
    path("search-items/", views.search_items, name="search_items"),
    path("manage-items/", views.manage_item_formset, name="manage_items"),  # type: ignore
]
