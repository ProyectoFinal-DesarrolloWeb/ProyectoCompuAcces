from django.db import models
from Apps.cliente.models import Cliente
from Apps.administracion.models import Producto
from Apps.usuarios.models import Empleado
from django.db.models.signals import m2m_changed

# Create your models here.
class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %s' % (self.fecha,self.cliente)

    # def update_totals (self):
    #     self.total = sum([ producto.precio for producto in self.producto.all()])
    #     self.save()    

class Cotizacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)

    def __str__(self):
        return '%s %s' % (self.fecha,self.total)


# def updateTotals (sender, instance, action, *args, **kwargs):
#     if action == "post_add" or action == "post_remove" or action == "post_clear":
#         instance.update_totals

# m2m_changed.connect(updateTotals, sender = Venta.producto.through)