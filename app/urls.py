from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("general_details/", views.general_details, name="general_details"),
]