from django.shortcuts import render
from .forms import ClienteForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

class ClienteView(TemplateView):
    template_name='client.html'

class CrearClienteView(CreateView):
    template_name="client.html"
    form_class=ClienteForm
    success_url= reverse_lazy('cliente:clientesapp')
# Create your views here.
