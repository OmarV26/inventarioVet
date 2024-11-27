from django.contrib import admin
from gestorProductos.models import Categoria, Producto

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'categoria')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)