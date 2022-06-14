from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.urls import path

from institute import views

app_name = 'institute'

urlpatterns = [
    path('', views.home, name="home"),
    path('course/search/', views.search, name="search"),
    path('course/teacher/<int:teacher_id>', views.teacher, name="teacher"),
    path('course/<int:course_id>/', views.course, name="course"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
