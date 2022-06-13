from django.shortcuts import render
from django.urls import path

from instituto import views

app_name = 'instituto'

urlpatterns = [
    path('', views.home, name="home"),
]
