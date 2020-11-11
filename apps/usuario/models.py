from django.db import models
from django.contrib.auth.models import User
from apps.rol.models import Rol
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import datetime


class UserManager(BaseUserManager):
    # rol=Rol.objects.get(pk=1)"""
    def create_user(self, username, email, password=None, rol=None):
        if self.objects is None:
            rol = Rol.model(id=1, nombre='administrador', descripcion='administrador del proyecto')
            rol.save()

        user = self.model(username=username, email=email, rol=rol)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # rol=Rol.objects.get(pk=1)"""
    def create_superuser(self, email, password, username='Prueba', rol=None):
        user = self.create_user(username=username, email=email, password=password, rol=Rol)
        if Rol.objects is None:
            rol = Rol.model(id=1, nombre='administrador', descripcion='administrador del proyecto')
            rol.save()
        else:
            rol = Rol.objects.get(pk=1)
        user.is_superuser = True
        user.save(using=self._db)
        return user

    # def get_by_natural_key(self, email_):
    # c   return self.get(code_number=email_)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, blank=True, unique=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIERED_FIELDS = ['username', 'rol', ]
    objects = UserManager()

    @classmethod
    def get_rol(self):
        return (self.rol)

    @classmethod
    def get_username(self):
        return self.username

    def __str__(self):
        return '{}'.format(self.username)
