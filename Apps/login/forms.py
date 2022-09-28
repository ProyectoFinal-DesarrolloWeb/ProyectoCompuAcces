from django import forms
from .models import Proveedor,Producto, Cliente, Cotizacion, Empleado, Venta

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = '__all__'

class CotizacionForm(forms.ModelForm):
    class Meta:
        model=Cotizacion
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields = '__all__'

class VentaForm(forms.ModelForm):
    class Meta:
        model=Venta
        fields = '__all__'