from django.shortcuts import render
from django.urls import path

from usuario import views

app_name = 'usuario'

urlpatterns = [
    path('', views.home, name="home"),
]
