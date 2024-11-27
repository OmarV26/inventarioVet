from django.urls import path
from gestorUser.views import *

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="registro"),
]