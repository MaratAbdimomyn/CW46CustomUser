from django.shortcuts import render, redirect
from .forms import Register
from .models import CustomUser
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.views import View

class ActiveUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_active == False:
            return redirect('register')
        return super().dispatch(request, *args, **kwargs)

class RegisterView(CreateView):
    model = CustomUser
    form_class = Register
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    
    def send_verification_email(self, user):
        token = default_token_generator.make_token(user)
        verify_url = self.request.build_absolute_uri(f'/verify/{user.pk}/{token}/')
        subject = 'Verify your email'
        message = f'Hello {user.username}, please click the link:\n\n{verify_url}'
        send_mail(subject, message, 'sender@example.com', [user.email])

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        user.is_active = False
        user.save()
        self.send_verification_email(user)
        return response

class VerifyEmailView(View):
    def get(self, request, user_pk, token):
        user = CustomUser.objects.get(pk=user_pk)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('positive')
        else:
            return redirect('negaitve')

class Positive(TemplateView):
    template_name = 'positive.html'

class Negative(TemplateView):
    template_name = 'negative.html'

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class Dashboard(TemplateView):
    template_name = 'dashboard.html'

"""class RegisterView(CreateView):
    model = CustomUser
    form_class = Register
    template_name = 'register.html'
    success_url = reverse_lazy('dashboard')"""

class UserList(ListView):
    model = CustomUser
    template_name = 'home.html'
    context_object_name = 'users'

class AboutUser(ActiveUserMixin, DetailView):
    model = CustomUser
    template_name = 'about.html'
    context_object_name = 'user'
