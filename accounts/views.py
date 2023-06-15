from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def hello_world(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
