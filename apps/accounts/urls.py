from django.urls import path

from .views import (
    login_user,
    register_user,
    search_non_profits,
    edit_org_info,
    edit_account_info,
    search_non_profits_results,
)

urlpatterns = [
    path("login/", login_user, name="login"),  # type: ignore
    path("register/", register_user, name="register"),
    path("search-non-profits/", search_non_profits, name="search_non_profits"),
    path("edit-org-info/", edit_org_info, name="edit_org_info"),  # type: ignore
    path("edit-account-info/", edit_account_info, name="edit_account_info"),  # type: ignore
    path(
        "search-non-profits-result/",
        search_non_profits_results,
        name="search_non_profits_results",
    ),
]
