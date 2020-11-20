from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from apps.tarea.models import Tarea
from apps.tarea.forms import TareaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.linea_base.models import LineaBase


@login_required
def index(request):
    return render(request, 'tarea/index.html')


class listar_tarea(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea/lista_proyectos.html'
    context_object_name = 'listar_tarea'
    paginate_by = 10


class crear_tarea(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/proyecto_form.html'
    success_url = reverse_lazy('listar_tarea')
    def get_form_kwargs(self):
        kwargs = super(crear_tarea, self).get_form_kwargs()
        # get users, note: you can access request using: self.request
        kwargs['Tarea'] = Tarea
        return kwargs


class eliminar_tarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'tarea/proyecto_delete.html'
    success_url = reverse_lazy('listar_tarea')
    context_object_name = 'eliminar_tarea'


class editar_tarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['version', 'prioridad', 'estado', 'descripcion', 'observacion', 'id_tarea_padre']
    template_name = 'tarea/proyecto_form.html'
    success_url = reverse_lazy('listar_tarea')
    def dispatch(self, request, *args, **kwargs):
        return super(editar_tarea,self).dispatch(request, *args, **kwargs)
