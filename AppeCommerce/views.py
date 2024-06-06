from django.shortcuts import render

from AppeCommerce.forms import ProductoForm

# Create your views here.
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'nombre_app/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la lista de productos o muestra un mensaje de éxito
    else:
        form = ProductoForm()
    return render(request, 'nombre_app/formulario_producto.html', {'form': form})