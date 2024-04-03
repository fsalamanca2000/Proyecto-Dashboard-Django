from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre = models.CharField(max_length=150)
    Barrio = models.CharField(max_length=120)
    Localidad = models.CharField(max_length=120)
    Fecha_de_compra = models.DateField()
    Nombre_Producto = models.CharField(max_length=120)
    Valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
