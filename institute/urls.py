from django.shortcuts import render
from django.urls import path

from institute import views

app_name = 'institute'

urlpatterns = [
    path('', views.home, name="home"),
]
