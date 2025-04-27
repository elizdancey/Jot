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
from .forms import ProfilePicForm
import json
from .models import JournalEntry
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404

@login_required
def main(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'home.html', {'entries': entries})


def options_menu(request):
    template = loader.get_template('options-menu.html')
    return HttpResponse(template.render())

def login(request):
    return render(request, 'login.html')

def registration(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('profile-update.html')
    return HttpResponse(template.render())

@login_required
def creation(request):
    return render(request, 'creation-space.html')

@csrf_protect
@login_required
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

@login_required
def edit_journal_entry(request, entry_id):
    entry = get_object_or_404(JournalEntry, id=entry_id, user=request.user)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        entry.title = data.get('title', entry.title)
        entry.content = data.get('content', entry.content)
        entry.save()
        return JsonResponse({'status': 'success', 'message': 'Entry updated.'})
    
    return JsonResponse({
        'id': entry.id,
        'title': entry.title,
        'content': entry.content,
        'created_at': entry.created_at,
    })

@login_required
def delete_journal_entry(request, entry_id):
    entry = get_object_or_404(JournalEntry, id=entry_id, user=request.user)
    
    if request.method == 'POST':
        entry.delete()
        return redirect('main')
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@login_required
def edit_journal_page(request, entry_id):
    entry = get_object_or_404(JournalEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        entry.title = title
        entry.content = content
        entry.save()

        return redirect('main')  # or 'journal_list'

    return render(request, 'edit.html', {'entry': entry})

@login_required
def settings(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ProfilePicForm(instance=profile)

    return render(request, 'settings.html', {'form': form})








