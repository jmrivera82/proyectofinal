from django.db import models

# Create your models here.

class maquinas(models.Model):
    nombre=models.CharField(max_length=50)
    empresa=models.CharField(max_length=20)
    
class juegos(models.Model):
    nombre=models.CharField(max_length=50)
    consola=models.CharField(max_length=20)
    año=models.IntegerField()
    
