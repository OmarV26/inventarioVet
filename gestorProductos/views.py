from django.shortcuts import render
from gestorProductos.forms import ProductoForm, CategoriaForm
from django.http import HttpResponseRedirect
from gestorProductos.models import Producto, Categoria
from django.urls import reverse

# Create your views here.


# Crear un nuevo producto
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

def agregarCategoria(request):
    form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            # Crear la nueva categoría
            nueva_categoria = Categoria.objects.create(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
            )
            return HttpResponseRedirect(reverse('agregarProducto'))
    else:
        form = CategoriaForm()
    return render(request, 'agregarCategoria.html', {'form': form})

#eliminar un producto
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return HttpResponseRedirect(reverse('productos'))



def productosView(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    data = {'productos': productos, 'categorias': categorias}
    return render(request, 'productosView.html', data)