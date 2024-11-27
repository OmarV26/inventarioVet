from django import forms
from gestorProductos.models import Categoria, Producto

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=200)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

    nombre.widget.attrs['class'] = 'form-control form-control-user' 'placeholder="Nombre del producto"'
    descripcion.widget.attrs['class'] = 'form-control form-control-user' 'placeholder="Descripción del producto"'
    precio.widget.attrs['class'] = 'form-control form-control-user' 'placeholder="Precio del producto"'
    categoria.widget.attrs['class'] = 'form-control form-control-user' 'placeholder="Categoria del producto"'


class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=200)

    nombre.widget.attrs['class'] = 'form-control form-control-user' 'placeholder="Nombre de la categoría"'
    descripcion.widget.attrs['class'] = 'form-control form-control-user' 'placeholder="Descripción de la categoría"'