from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('asignatura', views.asginatura, name='asignatura'),
    path('alumno', views.alumno, name='alumno'),
]