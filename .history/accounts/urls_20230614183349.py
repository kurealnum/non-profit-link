from django.urls import path
from . import views


url_patters = [
    path('helloworld/', views.members, name="hello_world"),
    ]