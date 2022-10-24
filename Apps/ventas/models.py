import uuid
from django.db import models
from Apps.administracion.models import Producto
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed, pre_save
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length= 100, null= False, blank = False, unique = True)
    empleado = models.ForeignKey(User, null=True, blank=True ,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)

    def __str__(self):
        return '%s %s' % (self.fecha,self.empleado)

    # def update_totals (self):
    #     self.total = sum([ producto.precio for producto in self.producto.all()])
    #     self.save()    

def set_cart_id(sender, instance, *arg, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

pre_save.connect(set_cart_id, sender = Cart)    

class Cotizacion(models.Model):
    empleado = models.ForeignKey(User,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    

    def __str__(self):
        return '%s %s' % (self.fecha,self.total)


# def updateTotals (sender, instance, action, *args, **kwargs):
#     if action == "post_add" or action == "post_remove" or action == "post_clear":
#         instance.update_totals

# m2m_changed.connect(updateTotals, sender = Venta.producto.through)