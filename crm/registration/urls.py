from django.contrib.auth import views as auth_views
from django.urls import path

from .views import RegisterView

app_name = "registration"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/", auth_views.LogoutView.as_view(http_method_names=["get", "post"]), name="logout"
    ),
    path("register/", RegisterView.as_view(), name="register"),
]
