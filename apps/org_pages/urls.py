from django.urls import path

from . import views

# NOT COMPLETE!!!
# homepage needs fancy URL stuff

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("homepage/", views.homepage, name="homepage"),
]
