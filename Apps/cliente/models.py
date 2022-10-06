from unittest.util import _MAX_LENGTH
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    nit = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    creacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)
# Create your models here.
