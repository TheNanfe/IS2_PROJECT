from django.db import models


class Rol(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
