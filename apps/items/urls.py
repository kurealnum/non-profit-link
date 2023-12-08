from django.urls import path

from . import views

urlpatterns = [
    path("search-items/", views.search_items, name="search_items"),
    path("api/", views.ItemListApiView.as_view()),
    path("api/<str:item_name>/", views.ItemListApiView.as_view()),
]
