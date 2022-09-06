from django.shortcuts import render
from django.views.generic import TemplateView
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