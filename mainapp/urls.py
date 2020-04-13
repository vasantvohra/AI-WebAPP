from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('about', views.about, name="about"),
    path('sign_verify', views.sign_verify, name="verification"),
    path('logout', views.logout, name="logout"),

]
