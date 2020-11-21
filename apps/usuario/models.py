from django.db import models
from django.contrib.auth.models import User
from apps.rol.models import Rol
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import datetime

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        user = self.model(username = username, email = email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username='Prueba'):
        user = self.create_user(username = username, email = email, password = password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=30, blank=True, unique=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)
    rol = models.ForeignKey(Rol, on_delete = models.CASCADE, blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIERED_FIELDS = ['username']
    objects  = UserManager()

    @classmethod
    def get_rol(self):
        return (self.rol)
        
    @classmethod
    def get_username(self):
        return self.username

    def __str__(self):
       return '{}'.format(self.username)
   