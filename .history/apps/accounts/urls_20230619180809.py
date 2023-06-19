from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.hello_world, name="login"),
]