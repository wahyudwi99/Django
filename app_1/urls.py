from django.urls import path

from . import views

urlpatterns = [
    path("home", views.index),
    path("login", views.login),
    path("login/login_result", views.login_output),
    path("test", views.test_aja)
]