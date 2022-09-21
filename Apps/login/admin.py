from django.contrib import admin
from .models import Cliente, Cotizacion, Empleado, Proveedor , Producto, Venta

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Venta)
admin.site.register(Cotizacion)
# Register your models here.
