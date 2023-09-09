from django.db import models

# Create your models here.

class Equipos(models.Model):
    codigoint=models.IntegerField()
    descripcion=models.CharField(max_length=50)
    tipo=models.CharField(max_length=15)
    marca=models.CharField(max_length=20)
    estado=models.CharField(max_length=10)

    def __str__ (self):
        return f"{self.codigoint} - {self.descripcion} - {self.estado}"
    
class Trabajos(models.Model):
    nombre=models.CharField(max_length=50)
    plataforma=models.CharField(max_length=20)
    
class Personal (models.Model):   
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    fecha_ingreso=models.DateField()
    email=models.EmailField()
    telefono=models.IntegerField()
    
    def __str__ (self):
        return f"{self.nombre} - {self.email}"

class Compras (models.Model):
    numfactura=models.IntegerField()
    monto=models.IntegerField()
    descripcion=models.CharField(max_length=50)

