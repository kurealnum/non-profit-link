from django.urls import path

from .views import login_user, logout_user, register_user

urlpatterns = [
    path("login/", login_user, name="login"),  # type: ignore
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
]
