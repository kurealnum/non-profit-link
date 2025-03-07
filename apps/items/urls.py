from django.urls import path

from apps.items.views import (
    RequestDataApiView,
    get_item,
    search_items,
    search_items_results,
)

urlpatterns = [
    # Django views
    path("search-items/", search_items, name="search_items"),  # type: ignore
    path("search-items-results/", search_items_results, name="search_items_results"),  # type: ignore
    path("item/<str:item_name>/", get_item, name="get_item"),
    # API Views
    path("manage-item/", RequestDataApiView.as_view(), name="manage_item"),
    path(
        "manage-item/<str:item_name>/",
        RequestDataApiView.as_view(),
        name="manage_item_with_name",
    ),
]
