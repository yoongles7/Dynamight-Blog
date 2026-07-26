from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("users/register", UserRegisterView.as_view(), name="register"),
    path("users/login", UserLoginView.as_view(), name="login"),
    path("users/logout", UserLogoutView.as_view(), name="logout"),
    path("users/refresh", TokenRefreshView.as_view(), name="refresh"),
]