# from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = "home"),
    path("uploads", views.uploads, name = "uploads"),
    path("run", views.run, name = "run"),
    path("robots.txt/", views.taunt, name="robots.txt"),
    path("secret/", views.taunt),
    path("admin/", views.taunt),
    path("forgotpassword/", views.taunt),
    path("resetpassword/", views.taunt),
    path("profile/", views.taunt),
    path("account/", views.taunt),
    path("test/", views.taunt),
    path("debug/", views.taunt),
    path("target.txt/", views.taunt), 
]
