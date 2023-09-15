from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('asignatura', views.asginatura, name='asignatura'),
    path('alumno', views.alumno, name='alumno'),
    path('registrarAsignatura', views.registrarAsignatura),
    path('registrarAlumno', views.registrarAlumno),
    path('eliminarAsignatura/<id>', views.eliminarAsignatura),
    path('eliminarAlumno/<id>', views.eliminarAlumno),

    path('edicionAsignatura/<id>', views.edicionAsignatura),
    path('edicionAlumno/<id>', views.edicionAlumno),

    path('editarAlumno', views.editarAlumno),
    path('editarAsignatura', views.editarAsignatura),
]