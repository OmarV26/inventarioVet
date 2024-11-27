from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "Usuario registrado correctamente"