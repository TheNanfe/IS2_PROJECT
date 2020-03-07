from django.views.generic.base import TemplateView
from django.shortcuts import render


class LoginView(TemplateView):
    template_name = "core/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
