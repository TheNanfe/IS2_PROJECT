from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from apps.tarea.models import Tarea, LineaBase
from apps.tarea.forms import TareaForm, LineaBaseForm
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
    print('esto siempre se ejecuta \n\n\n\n')
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


class listar_linea_base(LoginRequiredMixin, ListView):
    model = LineaBase
    fields = ['nombre', 'id_tarea']
    template_name = 'tarea/lista_lineabase.html'
    success_url = reverse_lazy('listar_lineabase')
    paginate_by = 10


class crear_linea_base(LoginRequiredMixin, CreateView):
    model = LineaBase
    form_class = LineaBaseForm
    template_name = 'tarea/lineabase_form.html'
    success_url = reverse_lazy('listar_lineabase')


class eliminar_linea_base(LoginRequiredMixin, DeleteView):
    model = LineaBase
    template_name = 'tarea/lineabase_delete.html'
    success_url = reverse_lazy('listar_lineabase')
    context_object_name = 'eliminar_lineabase'


class editar_linea_base(LoginRequiredMixin, UpdateView):
    model = LineaBase
    fields = ['nombre', 'id_tarea']
    template_name = 'tarea/lineabase_form.html'
    success_url = reverse_lazy('listar_lineabase')