from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "Usuario registrado correctamente"

def usuariosView(request):
    auth_user = User.objects.all()
    return render(request, 'usuarios.html', {'auth_user': auth_user})

def perfilview(request):
    return render(request, 'perfil.html')