from django.db import models

# Create your models here.

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    asignaturas = models.ManyToManyField(Asignatura, related_name='alumnos')

    def __str__(self):
        return self.nombre