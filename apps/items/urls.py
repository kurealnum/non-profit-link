from django.urls import path

from . import views

urlpatterns = [
    path("search-items/", views.search_items, name="search_items"),
    path("create-item/", views.SpecificItemApiView.as_view()),
    path("item/<str:item_name>/", views.SingleItemApiView.as_view()),
]
