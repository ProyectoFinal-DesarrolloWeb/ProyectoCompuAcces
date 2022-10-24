from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from .models import Cart 
from .utils import getOrCreateCart
from .forms import VentaForm

def cart(request): 
    cart = getOrCreateCart(request)
    form = VentaForm
    return render(request, 'ventas.html',{'form': form})


# from Apps.ventas.forms import VentaForm , CotizacionForm
# from Apps.ventas.models import Venta

# class CrearVentaView(CreateView):
#     template_name='ventas.html'
#     success_url= reverse_lazy('ventas:crearVenta')
#     form_class=VentaForm

# class ListarVentasView(ListView):
#     template_name="sales.html"
#     model = Venta


# class CotizacionView(TemplateView):
#     template_name='cotizacion.html'


# class CrearCotizacionView(CreateView):
#     template_name="cotizacion.html"
#     form_class=CotizacionForm
#     success_url= reverse_lazy('ventas:crearCotizacion')

    # def get_queryset(self):
        # return Venta.objects.all()

    # form_class=EmpleadoForm
    # success_url= reverse_lazy('usuarios:usuariosapp')