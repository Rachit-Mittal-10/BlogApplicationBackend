from django.urls import path, include

urlpatterns = [
    path("roles/",include("roles.urls")),
    path("users/",include("users.urls")),
    path("auth/",include("authentication.urls")),
]