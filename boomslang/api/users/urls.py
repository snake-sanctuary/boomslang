"""Urls for users profile and authentication."""

from django.urls import path

from users.views import login, signup
urlpatterns = [
    path("signup/", signup),
    path("login/", login),
]
