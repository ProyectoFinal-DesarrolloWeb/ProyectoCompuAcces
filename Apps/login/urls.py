"""SistemaCompuAcces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import loginview, HomeView, Login, Logout,  RegistroView
from Apps.login import views
from django.contrib.auth.views import LoginView

app_name='login'
from django.contrib.auth.decorators import login_required

urlpatterns = [
 path('home/', login_required(HomeView.as_view()), name='homeapp'),
 path('', Login, name='loginapp'),
 path('logout/', Logout, name='logoutapp'),

 path('registrar/',RegistroView.as_view(), name='registro'),
]
