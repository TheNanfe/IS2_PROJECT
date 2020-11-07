from apps.usuario.models import User
from django.urls import reverse_lazy
from apps.proyecto.urls import index
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.rol.models import Rol
from django.views import View

def prueba(allGood):
    print(User.get_rol())
    print(Rol.objects.all().filter(pk=1))
    if User.get_rol() == Rol.objects.all().filter(pk=1):
        return allGood

    class AllBad(View):
        def get(self, request):
            return  HttpResponseRedirect(reverse_lazy('index'))
    return AllBad



def decorator_factory(argument):
    if argument.get_rol() == Rol.objects.all().filter(pk=1): 
        def decorator(function):
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                return result
            return wrapper
        return decorator
    class AllBad(View):
        def get(self, request):
            return  HttpResponseRedirect(reverse_lazy('index'))
    return AllBad
