from django.db import models

# Create your models here.

class Equipos(models.Model):
    codigoint=models.IntegerField()
    producto=models.CharField(max_length=30)
    tipo=models.CharField(max_length=15)
    descripcion=models.CharField(max_length=50)
    marca=models.CharField(max_length=20)
    def __str__ (self):
        return f"{self.codigoint} - {self.producto} - {self.tipo}"
    
class Trabajos(models.Model):
    nombre=models.CharField(max_length=50)
    plataforma=models.CharField(max_length=20)
    
class Personal (models.Model):   
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    fecha_ingreso=models.DateTimeField()
    email=models.EmailField()
    telefono=models.IntegerField()

class Compras (models.Model):
    numfactura=models.IntegerField()
    monto=models.IntegerField()
    descripcion=models.CharField(max_length=50)

