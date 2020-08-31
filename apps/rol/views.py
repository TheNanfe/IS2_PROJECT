from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.rol.models import Rol
from apps.rol.forms import RegistroRol


class RegistroRol(CreateView):
    model = Rol
    template_name = "rol/registro.html"
    form_class = RegistroRol
    success_url = reverse_lazy("listar_rol")


class RolList(ListView):
    model = Rol
    template_name = 'rol/lista_roles.html'
    context_object_name = 'rol_list'
    paginate_by = 10


class EditarRol(UpdateView):
    model = Rol
    fields = ['nombre', 'descripcion']
    template_name = 'rol/rol_form.html'
    success_url = reverse_lazy("listar_rol")


class RolDelete(DeleteView):
    model = Rol
    template_name = 'rol/rol_delete.html'
    success_url = reverse_lazy('listar_rol')
    context_object_name = 'rol_delete'
