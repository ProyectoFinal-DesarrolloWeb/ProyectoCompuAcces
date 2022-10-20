from django import forms
from .models import  Cotizacion, Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model=Venta
        fields = '__all__'

class CotizacionForm(forms.ModelForm):
    class Meta:
        model=Cotizacion
        fields = '__all__'