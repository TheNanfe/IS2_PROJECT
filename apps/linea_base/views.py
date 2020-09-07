from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from apps.linea_base.models import LineaBase
from apps.linea_base.forms import LineaBaseForm
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