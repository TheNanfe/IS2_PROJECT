from django.db import models
from django.contrib.postgres.fields import ArrayField
from abc import ABCMeta


# Create your models here.
class Tarea(models.Model):
    version = models.CharField(max_length=50)
    prioridad_tarea = (
        ('Alta', 'Alta'),
        ('Med', 'Media'),
        ('Baja', 'Baja'),
    )
    prioridad = models.CharField(max_length=10, choices=prioridad_tarea)
    estado_tarea = (
        ('PEN', 'PENDIENTE'),
        ('FIN', 'FINALIZADO'),
        ('INI', 'INICIADO'),
    )
    estado = models.CharField(max_length=3, choices=estado_tarea)
    descripcion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50, null=True, blank=True)
    id_tarea_padre = models.ForeignKey('Tarea', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id, self.descripcion)



