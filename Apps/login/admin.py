from django.contrib import admin
from .models import Cliente, Cotizacion, Empleado, Proveedor , Product, Venta, Categoria

admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Product)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Venta)
admin.site.register(Cotizacion)
# Register your models here.
