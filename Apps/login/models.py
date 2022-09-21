from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=45)
    nit = models.CharField(max_length=10)
    creacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.nombre,self.nit)




class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    icono = models.ImageField()
    proveedor = models.ManyToManyField(Proveedor)
    creacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.nombre,self.descripcion)


class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    nit = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    creacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class Empleado(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=10)
    usuario = models.CharField(max_length=15)
    contrasenia = models.CharField(max_length=250) 
    tipo_empleado = (
        ('v','Vendedor'),
        ('a','Administrador'),
    )
    tipo = models.CharField(
        max_length= 1, 
        choices=tipo_empleado,
        default='v',
    )
    estado_disponibilidad = (
        ('a','Activo'),
        ('i','Inactivo'),
    )
    disponibilidad = models.CharField(
        max_length= 1,
        choices=estado_disponibilidad,
        default= 'a',
    )
    creacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.usuario,self.tipo)

class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s' % (self.fecha,self.cliente)

class Cotizacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)

    def __str__(self):
        return '%s %s' % (self.fecha,self.total)
