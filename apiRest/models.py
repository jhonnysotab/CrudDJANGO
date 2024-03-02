from django.db import models

# Create your models here.
class Alumno(models.Model):
    fullname = models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    grado   = models.CharField(max_length=45)
    seccion = models.CharField(max_length=2)
    edad = models.IntegerField()
    is_active = models.BooleanField(default=True)
    