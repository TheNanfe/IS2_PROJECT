from django.db import models
from django.contrib.auth.models import User, AbstractUser
from apps.rol.models import Rol


class UsuarioSistema(AbstractUser):
    Rol = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)
    "Se crea el modelo UsuarioSistema, tiene una relacion one to one field con user, se agrega el campo rol" \
    "de este modo se extiende del modelo User"
