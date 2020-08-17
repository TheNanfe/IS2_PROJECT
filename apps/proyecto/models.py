from django.db import models

# Create your models here.
class Proyecto(models.Model):
    Proyecto_id = models.CharField(max_length = 10, primary_key=True) 
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 50)