from django.contrib import admin
from django.urls import path, include
from health_check.views import HealthCheckView

urlpatterns = [
    path("", include("apps.blog.urls")),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("health/", HealthCheckView.as_view()),
]
