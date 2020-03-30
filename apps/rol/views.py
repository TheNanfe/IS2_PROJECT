#from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from apps.proyecto.urls import index
from apps.rol.models import Rol
from apps.rol.forms import RegistroRol


class RegistroRol(CreateView):
    model = Rol
    template_name = "rol/registro.html"
    form_class = RegistroRol
    success_url = reverse_lazy("Listar")



class RolList(LoginRequiredMixin,ListView):
    model = Rol
    template_name = 'rol/lista_roles.html'
    context_object_name = 'rol_list'
    paginate_by = 10


class EditarRol(LoginRequiredMixin, UpdateView):
    model = Rol
    fields = ['nombre', 'descripcion']
    template_name = 'rol/rol_form.html'
    success_url = reverse_lazy("Listar")


class RolDelete(LoginRequiredMixin, DeleteView):
    model = Rol
    template_name = 'rol/rol_delete.html'
    success_url = reverse_lazy('Listar')
    context_object_name = 'rol_delete'
