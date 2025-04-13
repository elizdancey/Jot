from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
 

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = "registration/registration.html"