from datetime import date, timedelta
from io import BytesIO

from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from apps.rol.models import Rol
from django.contrib.auth.decorators import login_required
from apps.tarea.models import Tarea
from apps.tarea.forms import TareaForm
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    return render(request, 'tarea/index.html')

'''def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarea')
    else:
        form = TareaForm()
    return render(request, 'tarea/lista_proyectos.html', {'form': form})'''

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
