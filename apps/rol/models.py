from django.db import models
from django.contrib.postgres.fields import ArrayField

class Rol(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=100, null=True)
    choices = models.CharField(max_length=300, null=True, blank=True)
    

    def get_id(self):
        return self.id
    
    def __str__(self):
       return '{}'.format(self.nombre)
