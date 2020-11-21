from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from apps.linea_base.models import LineaBase
from apps.linea_base.forms import LineaBaseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from apps.rol.models import Rol
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

PERMISO_CREATE = 'lb_cre'
PERMISO_LIST = 'lb_list'
PERMISO_EDIT = 'lb_edit'
PERMISO_DELETE = 'lb_del'


@login_required
def index(request):
    return render(request, 'tarea/index.html')


class listar_linea_base(LoginRequiredMixin, ListView):
    model = LineaBase
    fields = ['nombre', 'id_proyecto']
    template_name = 'tarea/lista_lineabase.html'
    success_url = reverse_lazy('listar_lineabase')
    paginate_by = 10
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                    user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol.get_id()))
                except:
                    raise PermissionDenied("No tiene los permisos adecuados")
                if (PERMISO_LIST in user_rol or PERMISO_EDIT in user_rol or 
                PERMISO_DELETE in user_rol or request.user.is_superuser):
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(listar_linea_base, self).dispatch(request,*args,**kwargs)


class crear_linea_base(LoginRequiredMixin, CreateView):
    model = LineaBase
    form_class = LineaBaseForm
    template_name = 'tarea/lineabase_form.html'
    success_url = reverse_lazy('listar_lineabase')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol.get_id()))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if PERMISO_CREATE in user_rol:
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(crear_linea_base, self).dispatch(request,*args,**kwargs)


class eliminar_linea_base(LoginRequiredMixin, DeleteView):
    model = LineaBase
    template_name = 'tarea/lineabase_delete.html'
    success_url = reverse_lazy('listar_lineabase')
    context_object_name = 'eliminar_lineabase'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol.get_id()))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if PERMISO_CREATE in user_rol:
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(eliminar_linea_base, self).dispatch(request,*args,**kwargs)


class editar_linea_base(LoginRequiredMixin, UpdateView):
    model = LineaBase
    fields = ['nombre', 'id_tarea']
    template_name = 'tarea/lineabase_form.html'
    success_url = reverse_lazy('listar_lineabase')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol.get_id()))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if PERMISO_CREATE in user_rol:
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(editar_linea_base, self).dispatch(request,*args,**kwargs)