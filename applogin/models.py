from django.db import models
from .views import *

# Create your models here.


class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)