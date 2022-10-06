from django.shortcuts import render
from .forms import ProveedorForm, ProductoForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
# Create your views here.
class ProveedorView(TemplateView):
    template_name='providers.html'

class ProductosView(TemplateView):
    template_name='products.html'


class CrearProveedorView(CreateView):
    template_name="providers.html"
    form_class=ProveedorForm
    success_url= reverse_lazy('administracion:proveedorapp')

class CrearProductoView(CreateView):
    template_name="products.html"
    form_class=ProductoForm
    success_url= reverse_lazy('administracion:productosapp')