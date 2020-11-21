from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from apps.usuario.forms import RegistroForm, RegistroFormNewUser
from apps.proyecto.urls import index
from apps.usuario.models import User, UserManager
from apps.usuario.decorator import *
from django.contrib.auth.decorators import user_passes_test
from apps.rol.models import Rol
from django.core.exceptions import PermissionDenied

PERMISO_CREATE = 'user_cre'
PERMISO_LIST = 'user_list'
PERMISO_EDIT = 'user_edit'
PERMISO_DELETE = 'user_del'


class RegistroForm(CreateView):
    model = User
    template_name = "usuario/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy("listar_usuario")
   
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol))
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
        return super(RegistroForm, self).dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        email = form.cleaned_data['email']
        form.instance.email = email
        return super(RegistroForm,self).form_valid(form)


class RegistroNuevo(CreateView):
    model = User
    template_name = "usuario/usuario_form.html"
    form_class = RegistroFormNewUser
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.rol = None
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        email = form.cleaned_data['email']
        form.instance.email = email
        return super(RegistroNuevo,self).form_valid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "core/login.html"
    success_url = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class UsuarioList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuario/lista_usuarios.html'
    context_object_name = 'user_list'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if (PERMISO_LIST in user_rol or PERMISO_EDIT in user_rol or 
                PERMISO_DELETE in user_rol or request.user.is_superuser):
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(UsuarioList, self).dispatch(request,*args,**kwargs)


class editarUsuario(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    #template_class = RegistroFormNewUser
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy("listar_usuario")
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:  
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if PERMISO_EDIT in user_rol or request.user.is_superuser:
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
        return super(editarUsuario, self).dispatch(request,*args,**kwargs)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        email = form.cleaned_data['email']
        form.instance.email = email
        return super(editarUsuario,self).form_valid(form)

    
class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('listar_usuario')
    context_object_name = 'usuario_delete'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            def controlador(request):
                try:
                   user_rol = Rol.objects.values_list('choices', flat=True).get(pk=str(request.user.rol))
                except:
                    raise PermissionDenied("Los passwords no coinciden")
                if PERMISO_DELETE in user_rol or request.user.is_superuser:
                    print('felicidades')
                    return 0
                else:
                    print(request.user.rol)
                    return 1
            if controlador(request) == 1:
                return HttpResponseRedirect(reverse_lazy('index'))
            
        return super(UsuarioDelete, self).dispatch(request,*args,**kwargs)



