from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, AbstractUser
from apps.usuario.models import UsuarioSistema
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect

from apps.usuario.forms import RegistroForm
from apps.proyecto.urls import index


class RegistroForm(CreateView):
    model = UsuarioSistema
    template_name = "usuario/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy("index")


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "core/login.html"
    success_url = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
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
    model = UsuarioSistema
    template_name = 'usuario/lista_usuarios.html'
    context_object_name = 'user_list'
    paginate_by = 10


class editarUsuario(LoginRequiredMixin, UpdateView):
    model = UsuarioSistema
    fields = ['username', 'first_name', 'last_name', 'email', 'Rol']
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy("index")



"""def editarUsuario(request, pk):
    usuario = User.objects.get(id=pk)
    if request.method == 'GET':
        usuario_form = RegistroForm(instance=usuario)
    else:
        usuario_form = RegistroForm(request.POST, instance=usuario)
        if usuario_form.is_valid():
            return redirect('lista_usuario')
        else:
            usuario_form = RegistroForm()
    return render(request, 'usuario/usuario_form.html', {'form': usuario_form})"""


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = UsuarioSistema
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('lista_usuario')
    context_object_name = 'usuario_delete'
