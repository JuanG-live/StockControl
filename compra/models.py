from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)

    def __str__(self):
        return self.apellido
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name= "producto")

    def __str__(self):
        return self.nombre
    