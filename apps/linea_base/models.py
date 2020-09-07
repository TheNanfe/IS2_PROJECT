from django.db import models
from apps.tarea.models import Tarea


class LineaBase(models.Model):
    nombre = models.CharField(max_length=50)
    id_tarea = models.ManyToManyField(Tarea, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
