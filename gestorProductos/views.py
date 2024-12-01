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
                user=request.user
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

#editar un producto
def editarProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)  # Obtener el producto por su ID
    except Producto.DoesNotExist:
        return HttpResponseRedirect(reverse('productos'))  # Redirigir si no existe

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Actualizar el producto
            producto.nombre = form.cleaned_data['nombre']
            producto.descripcion = form.cleaned_data['descripcion']
            producto.precio = form.cleaned_data['precio']
            producto.categoria = form.cleaned_data['categoria']
            producto.save()
            return HttpResponseRedirect(reverse('productos'))
    else:
        # Prellenar el formulario con los datos del producto
        form = ProductoForm(initial={
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'categoria': producto.categoria
        })

    return render(request, 'editarProducto.html', {'form': form, 'producto': producto})


def productosView(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(user=request.user)
        
    categorias = Categoria.objects.all()
    data = {'productos': productos, 'categorias': categorias}
    return render(request, 'productosView.html', data)