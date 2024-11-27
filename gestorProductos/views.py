from django.shortcuts import render
from gestorProductos.forms import ProductoForm
from django.http import HttpResponseRedirect
from gestorProductos.models import Producto, Categoria
from django.urls import reverse

# Create your views here.

def agregarProducto(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Crear el nuevo producto
            nuevo_producto = Producto.objects.create(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                categoria=form.cleaned_data['categoria'],

            )
            return HttpResponseRedirect(reverse('productos'))
    else:
        form = ProductoForm()
    categorias = Categoria.objects.all()

    
    

    return render(request, 'agregarProducto.html', {'form': form, 'categorias': categorias})

def productosView(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    data = {'productos': productos, 'categorias': categorias}
    return render(request, 'productosView.html', data)