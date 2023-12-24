from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),  # type: ignore
    path("homepage/<str:org_name>/", views.homepage, name="homepage"),  # type: ignore
    path(
        "homepage/error/org_does_not_exist",
        views.org_does_not_exist,
        name="org_does_not_exist",
    ),
]
