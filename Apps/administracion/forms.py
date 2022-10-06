from django import forms
from .models import Proveedor,Producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields = '__all__'