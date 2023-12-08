from django.urls import path

from . import views

urlpatterns = [
    path("search-items/", views.search_items, name="search_items"),
    path("manage-item/", views.SpecificItemApiView.as_view()),
    path("manage-item/<str:item_name>/", views.SingleItemApiView.as_view()),
]
