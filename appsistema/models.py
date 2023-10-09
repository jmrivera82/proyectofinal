from django.db import models
from django.contrib.auth.models import User

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
    equipo=models.CharField(max_length=50, default='PC')
    oficina=models.CharField(max_length=20)
    personal=models.CharField(max_length=50, null=True)
    descripcion=models.CharField(max_length=50)
    fecha_inicio=models.DateField(null=True)
    fecha_termino=models.DateField(null=True)
        
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
    proveedor=models.CharField(max_length=50, default='proveedor')
    def __str__ (self):
        return f"{self.numfactura} - {self.monto} - {self.proveedor}"

#class Avatar(models.Model):
#    imagen=models.ImageField(upload_to="avatars")
#    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)