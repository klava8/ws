from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Profile, Wallet
from .forms import ProfileRegForm, ProfileLoginForm
from django.urls import reverse_lazy


class ProfileRegView(CreateView):
    template_name = 'profile_register.html'
    model = Profile
    form_class = ProfileRegForm
    success_url = reverse_lazy('') # На страницу профиля

    def form_valid(self, form):



        return super().form_valid(form) 

class ProfileLoginView(LoginView):
    template_name = 'profile_login.html'
    success_url = reverse_lazy('') # На страницу профиля

class ProfileLogoutView(LogoutView):
    template_name = 'profile_logout.html'
    