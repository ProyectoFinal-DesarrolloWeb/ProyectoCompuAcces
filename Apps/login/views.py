from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
# Create your views here.

class LoginView(TemplateView):
    template_name='index.html'

class HomeView(TemplateView):
    template_name='home.html'
