from django.shortcuts import render

from .models import Cube


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cubes_index(request):
    return render(request, 'cubes/index.html', {'cubes': cubes})