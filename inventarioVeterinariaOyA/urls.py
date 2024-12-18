"""
URL configuration for inventarioVeterinariaOyA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from gestorProductos.views import *
from gestorUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", index, name="index"),
    path("index/", index, name="index"),
    path("usuarios/", include("gestorUser.urls")),
    path("agregarProducto/", agregarProducto, name="agregarProducto"),
    path("productos/", productosView , name="productos"),
    path("eliminarProducto/<int:id>/", eliminarProducto, name="eliminarProducto"),
    path("editarProducto/<int:id>/", editarProducto, name="editarProducto"),
    path("agregarCategoria/", agregarCategoria, name="agregarCategoria"),
    path("eliminarCategoria/<int:id>/", eliminarCategoria, name="eliminarCategoria"),
    path("categorias/", categoriasView, name="categorias"),
    path("editarCategoria/<int:id>/", editarCategoria, name="editarCategoria"),
    path("usuarios/", usuariosView, name="usuarios"),
    path("perfil/", perfilview, name="perfil"),
]
