from django.urls import include, path
from AppCoder import views
from django.contrib import admin


urlpatterns = [
    path("", views.inicio),
    path('cursos', views.cursos, name='Cursos'),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
]