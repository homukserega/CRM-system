from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    MyLogoutView,
    AboutMeView,
    RegisterView,

)

app_name = "registration"


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),
]