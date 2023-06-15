from django.urls import path
from . import views

url_patterns = [
    path('helloworld/', views.hello_world, name="hello_world"),
]