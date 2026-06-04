from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("generalDetails/", views.general_details, name="general_details"),
]