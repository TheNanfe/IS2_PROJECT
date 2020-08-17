from django.db import models

class Rol(models.Model):
    Rol_id = models.CharField(max_length = 10 , primary_key = True)
    nombre = models.CharField(max_length = 100, null=False)
    descripcion = models.CharField(max_length = 100, null=True)
   

