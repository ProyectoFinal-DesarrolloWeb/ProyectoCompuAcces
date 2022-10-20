from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from Apps.ventas.forms import VentaForm
from Apps.ventas.models import Venta

class CrearVentaView(CreateView):
    template_name='ventas.html'
    success_url= reverse_lazy('ventas:crearVenta')
    form_class=VentaForm

class ListarVentasView(ListView):
    template_name="sales.html"
    model = Venta


    # def get_queryset(self):
        # return Venta.objects.all()

    # form_class=EmpleadoForm
    # success_url= reverse_lazy('usuarios:usuariosapp')