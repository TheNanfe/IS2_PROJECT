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
from apps.proyecto.models import Proyecto
from apps.proyecto.forms import ProyectoForm
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    return render(request, 'proyecto/index.html')


class proyecto_list(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'proyecto/lista_proyectos.html'
    context_object_name = 'proyecto_list'
    paginate_by = 10


class proyecto_create(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto/proyecto_form.html'
    success_url = reverse_lazy('listar_proyecto')


class proyecto_delete(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'proyecto/proyecto_delete.html'
    success_url = reverse_lazy('listar_proyecto')
    context_object_name = 'proyecto_delete'


class proyecto_edit(LoginRequiredMixin, UpdateView):
    model = Proyecto
    fields = ['nombre', 'codigo', 'fecha_inicio', 'fecha_fin', 'estado', 'sprint', 'tarea', 'cliente']
    template_name = 'proyecto/proyecto_form.html'
    success_url = reverse_lazy('listar_proyecto')
