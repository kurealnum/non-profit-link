from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.hello_world, name="register"),
]