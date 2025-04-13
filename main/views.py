from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from .models import *

def main(request):
    return render(request, 'home.html')

def options_menu(request):
    template = loader.get_template('options-menu.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
    

def registration(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render())

def settings(request):
    template = loader.get_template('settings.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('profile-update.html')
    return HttpResponse(template.render())

def creation(request):
    template = loader.get_template('creation-space.html')
    return HttpResponse(template.render())




