from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("volunteer.urls")),
    path('turtle/', admin.site.urls),
]
