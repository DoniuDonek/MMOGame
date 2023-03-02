# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.views.generic import CreateView
# from django.urls import reverse_lazy
# from .forms import SignUpForm

# class SignUpPageView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('home')
#     template_name = 'registration/signup.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.success_url)

from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = "home.html"
class AboutPageView(TemplateView): 
    template_name = "about.html"

class LoginPageView(TemplateView):
    template_name = "account/login.html"

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html"