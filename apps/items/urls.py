from django.urls import path

from . import views

urlpatterns = [
    path("search-items/", views.search_items, name="search_items"),
    path("manage-item/", views.PostPutItemApiView.as_view()),
    path("manage-item/<str:item_name>/", views.GetDeleteItemApiView.as_view()),
]
