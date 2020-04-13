from django.contrib import admin
from django.urls import path, include

import signature_ver
from . import views

urlpatterns = [

    path('', views.index, name="index"),

]
