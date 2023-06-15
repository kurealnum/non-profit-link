from django.urls import path
from . import views

url_patterns = [
    path('helloworld/', views.members, name="hello_world"),
    ]