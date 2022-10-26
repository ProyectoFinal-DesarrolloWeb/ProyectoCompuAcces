from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from .models import CartProducts, Venta
from .utils import getOrCreateCart, destroyCart
from .forms import VentaForm
from Apps.administracion.models import Producto


def cart(request): 
    cart = getOrCreateCart(request)
    
    return render(request, 'ventas.html',{'cart': cart})

def add(request):
    cart = getOrCreateCart(request)
    product = Producto.objects.get(pk = request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    cart_product = CartProducts.objects.createOrUpdateQuantity(cart=cart, product=product , quantity=quantity)

    # cart.producto.add(product, through_defaults={
    #     'quantity':quantity
    # })

    return render(request, 'agregar.html', {'product': product}) 

def remove(request):
    cart = getOrCreateCart(request)
    product = Producto.objects.get(pk = request.POST.get('product_id'))
    cart.producto.remove(product)

    return redirect('ventas:cart')

def complete(request):
    cart = getOrCreateCart(request)
    productos = Producto.objects.filter(nombre = cart.producto)
    venta = Venta.objects.create(empleado= cart.empleado, fecha = cart.fecha, total = cart.total)

    venta.producto.set(cart.producto.all())
    
    destroyCart(request)

    return redirect('ventas:sales')

class VentasListView(ListView):
    template_name='sales.html'
    model = Venta
