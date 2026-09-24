from django.contrib import admin
from django.urls import path
from social.views import home, login_view, logout_view, register, profile


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
    path("profile/<str:username>/", profile, name="profile"),
]