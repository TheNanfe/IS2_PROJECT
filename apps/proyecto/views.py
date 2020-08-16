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


@login_required
def index(request):
    return render(request, 'proyecto/index.html')
