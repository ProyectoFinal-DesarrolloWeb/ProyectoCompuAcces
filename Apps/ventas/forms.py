from django import forms
from .models import Cart

class VentaForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields = '__all__'

# class CotizacionForm(forms.ModelForm):
#     class Meta:
#         model=Cotizacion
#         fields = '__all__'