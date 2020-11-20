from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from apps.linea_base.models import LineaBase
from apps.linea_base.forms import LineaBaseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
PERMISO_VISTA_USER = ['administrador','desarrollador']


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
    '''def dispatch(self, *arg, **kwargs):
        print(LineaBase.objects.filter(id_tarea=12))
        return super(listar_linea_base, self).dispatch(*arg, **kwargs)'''
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
    '''def dispatch(self, request, *args, **kwargs):
        def controlador(request):
            print(LineaBase.objects.filter(pk=kwargs.pop('pk', None)))
            print(args)
            #cleaned_data = super(eliminar_linea_base, self).clean()
            print(kwargs.pop('pk', None))
            if str(request.LineaBase.id_tarea) in PERMISO_VISTA_USER:
                print('felicidades')
                return 0
            else:
                print(request.LineaBase.id_tarea)
                return 1
        if controlador(request) == 1:
            return HttpResponseRedirect(reverse_lazy('index'))
        
        return super(eliminar_linea_base, self).dispatch(request,*args,**kwargs)'''


class editar_linea_base(LoginRequiredMixin, UpdateView):
    model = LineaBase
    fields = ['nombre', 'id_tarea']
    template_name = 'tarea/lineabase_form.html'
    success_url = reverse_lazy('listar_lineabase')
    '''def dispatch(self, request, *args, **kwargs):
        print('hola!!!!')
        print('hola!!!!')
        print('hola!!!!')
        print('hola!!!!')
        print('hola!!!!')
        print(kwargs)
        print('\n\n',request,'\n\n')
        return super(editar_linea_base, self).dispatch(request, *args, **kwargs)'''