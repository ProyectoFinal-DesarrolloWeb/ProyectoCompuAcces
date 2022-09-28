from django.shortcuts import render
from .forms import ProveedorForm, ProductoForm, ClienteForm,CotizacionForm, EmpleadoForm, VentaForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
# Create your views here.

class LoginView(TemplateView):
    template_name='index.html'

class HomeView(TemplateView):
    template_name='home.html'

class ClienteView(TemplateView):
    template_name='client.html'

class ProveedorView(TemplateView):
    template_name='providers.html'

class ProductosView(TemplateView):
    template_name='products.html'

class UsuariosView(TemplateView):
    template_name='admin.html'

class VentasView(TemplateView):
    template_name='ventas.html'

class VentasListView(TemplateView):
    template_name='sales.html'

class CotizacionView(TemplateView):
    template_name='cotizacion.html'


class CrearProveedorView(CreateView):
    template_name="providers.html"
    form_class=ProveedorForm
    success_url= reverse_lazy('login:homeapp')

class CrearProductoView(CreateView):
    template_name="products.html"
    form_class=ProductoForm
    success_url= reverse_lazy('login:homeapp')

class CrearClienteView(CreateView):
    template_name="client.html"
    form_class=ClienteForm
    success_url= reverse_lazy('login:homeapp')

class CrearCotizacionView(CreateView):
    template_name="cotizacion.html"
    form_class=CotizacionForm
    success_url= reverse_lazy('login:homeapp')

class CrearEmpleadoView(CreateView):
    template_name="admin.html"
    form_class=EmpleadoForm
    success_url= reverse_lazy('login:homeapp')

class CrearVentaView(CreateView):
    template_name="ventas.html"
    form_class=VentaForm
    success_url= reverse_lazy('login:homeapp')