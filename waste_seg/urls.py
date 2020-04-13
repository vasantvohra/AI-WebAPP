from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [

    path('',views.index , name="index"),
    path('answer/<int:id>',views.answer, name='answer')
    #path('upload',views.upload , name="upload"),

]
