from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def main(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


