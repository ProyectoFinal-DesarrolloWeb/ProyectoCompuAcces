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
from .views import LoginView, HomeView, ClienteView, ProveedorView, ProductosView,UsuariosView,VentasView,VentasListView, CotizacionView
from Apps.login import views
from .views import CrearProveedorView, CrearProductoView,CrearClienteView, CrearCotizacionView, CrearEmpleadoView, CrearVentaView
app_name='login'

urlpatterns = [
 path('', LoginView.as_view(), name='loginapp'),
 path('home/', HomeView.as_view(), name='homeapp'),
 path('clientes/', ClienteView.as_view(), name='clientesapp'),
 path('proveedor/', ProveedorView.as_view(), name='proveedorapp'),
 path('productos/', ProductosView.as_view(), name='productosapp'),
 path('usuarios/', UsuariosView.as_view(), name='usuariosapp'),
 path('ventas/', VentasView.as_view(), name='ventasapp'),
 path('ventaslist/', VentasListView.as_view(), name='ventaslistapp'),
 path('cotizacion/',CotizacionView.as_view(), name='cotizacionapp'),

  path('crearProveedor/',CrearProveedorView.as_view(), name='crearproveedor'),
  path('crearProducto/',CrearProductoView.as_view(), name='crearproducto'),
  path('crearCliente/',CrearClienteView.as_view(), name='crearcliente'),
  path('crearCotizacion/',CrearCotizacionView.as_view(), name='crearcotizacion'),
  path('crearEmpleado/',CrearEmpleadoView.as_view(), name='crearempleado'),
  path('crearVenta/',CrearVentaView.as_view(), name='crearventa'),
]
