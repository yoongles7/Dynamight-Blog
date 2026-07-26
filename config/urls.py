from django.contrib import admin
from django.urls import path, include
from health_check.views import HealthCheckView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("", include("apps.blog.urls")),
    path("", include("apps.users.urls")),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("health/", HealthCheckView.as_view()),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
