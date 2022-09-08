from django.db import models


class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    precio =models.FloatField(default=1)
    fecha  =models.DateTimeField()
    descripcion = models.CharField(max_length=50, default="-")

    def __str__(self) :
        return self.nombre


class Categoria(models.Model):
    hidraulico = models.CharField(max_length=30)
    Neumatico =models.FloatField(default=1)
    Electrico  =models.DateTimeField()
    otros = models.CharField(max_length=50, default="-")

    def __str__(self) :
        return self.nombre
        