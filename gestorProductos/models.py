from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos" )
    user = models.ForeignKey(User , on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre}"

