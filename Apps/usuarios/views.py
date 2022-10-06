from django.shortcuts import render
from .forms import EmpleadoForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

class UsuariosView(TemplateView):
    template_name='admin.html'

class CrearEmpleadoView(CreateView):
    template_name="admin.html"
    form_class=EmpleadoForm
    success_url= reverse_lazy('usuarios:usuariosapp')
# Create your views here.
