from django.urls import path

import views

urlpatterns = [
    path("login/", views.login_user, name="login"),  # type: ignore
    path("register/", views.register_user, name="register"),
    path("search-non-profits/", views.search_non_profits, name="search_non_profits"),
    path("edit-org-info/", views.edit_org_info, name="edit_org_info"),  # type: ignore
    path("edit-account-info/", views.edit_account_info, name="edit_account_info"),  # type: ignore
    path(
        "search-non-profits-result/",
        views.search_non_profits,
        name="search_non_profits_results",
    ),
]
