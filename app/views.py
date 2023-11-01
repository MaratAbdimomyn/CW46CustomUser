from django.shortcuts import render
from .forms import Register
from .models import CustomUser
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class Dashboard(TemplateView):
    template_name = 'dashboard.html'

class RegisterView(CreateView):
    model = CustomUser
    form_class = Register
    template_name = 'register.html'
    success_url = reverse_lazy('dashboard')