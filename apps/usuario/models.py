from django.db import models 

class Usuario(models.Model):
    Usuario_id = models.CharField(max_length = 10 , primary_key = True)
    nombre = models.CharField(max_length = 50) 
    descripcion = models.CharField(max_length = 50)    