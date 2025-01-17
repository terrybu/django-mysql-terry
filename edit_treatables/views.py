from django.shortcuts import render
from django.http import HttpResponse
from .models import Treatables

def index(request):
    context = {'title': 'Home Page'}
    return render(request, 'edit_treatables/index.html', context)