from django.urls import path

from . import views

urlpatterns = [
    path("credits/", views.credits, name="credits"),
    path("about-us/", views.about_us, name="about_us"),
    path("faq/", views.faq, name="faq"),
    path("", views.index, name="index"),
]
