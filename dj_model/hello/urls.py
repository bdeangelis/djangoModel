from django.urls import path
from hello import views

urlpattern = [
    path("", views.home, name="home"),
]