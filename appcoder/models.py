from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()
    def __str__ (self):
        return f"{self.nombre} - {self.comision}"
    
    
class Estudiantes(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.CharField(max_length=50)
    email=models.EmailField()
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.nombre} - {self.apellido}"



class Entregable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()
    
    

#clases para proyecto final
#usuarios

#Cursos 
class Oficinas(models.Model): 
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=30)
    telefono=models.IntegerField()
    
#estudiantes
class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    oficina=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    email=models.EmailField()
    
#entregables
class Trabajos(models.Model):
    solicitud=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)
    fecha_reporte=models.DateTimeField()
    fecha_realiza=models.DateTimeField()
    entregado=models.BooleanField()

#profesores
class Equipos(models.Model):
    tipoequipo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__ (self):
        return f"{self.nombre} - {self.apellido}"
    