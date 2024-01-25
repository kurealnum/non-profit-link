from django.urls import path

from . import views

urlpatterns = [
    path("search-items/", views.search_items, name="search_items"),  # type: ignore
    path("search-items-results/", views.search_items_results, name="search_items_results"),  # type: ignore
    path("manage-item/", views.RequestDataApiView.as_view(), name="manage_item"),
    path(
        "manage-item/<str:item_name>/",
        views.UrlDataApiView.as_view(),
        name="manage_item_with_name",
    ),
]
