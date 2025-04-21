from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import JournalEntry


def main(request):
    return render(request, 'home.html')

def options_menu(request):
    template = loader.get_template('options-menu.html')
    return HttpResponse(template.render())

def login(request):
    return render(request, 'login.html')

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

@csrf_exempt
def create_journal_entry(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')

        if request.user.is_authenticated:
            entry = JournalEntry.objects.create(
                user = request.user,
                title = title,
                content = content
            )
            return JsonResponse({'status': 'success', 'entry_id': entry.id})
        else: 
            return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=401)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)




