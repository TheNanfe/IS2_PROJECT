from django.db import models
from django.contrib.auth.models import User
from apps.rol.models import Rol
from django.contrib.auth.base_user import AbstractBaseUser
import datetime


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(default=datetime.date.today)
    rol = models.ForeignKey(Rol, on_delete = models.CASCADE)
    USERNAME_FIELD = 'username'