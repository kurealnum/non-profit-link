from django.urls import path

from . import views

urlpatterns = [
    path("search-items/", views.search_items, name="search_items"),
    path("add-item/<str:item_name>/", views.add_item, name="add_item"),  # type: ignore
    path("delete-item/<str:item_name>/", views.delete_item, name="delete_item"),  # type: ignore
]
