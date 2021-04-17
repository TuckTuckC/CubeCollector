from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cube


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cubes_index(request):
    cubes = Cube.objects.all()
    return render(request, 'cubes/index.html', {'cubes': cubes})

def cube_detail(request, cube_id):
    cube = Cube.objects.get(id=cube_id)
    return render(request, 'cubes/detail.html', {'cube': cube})

class CubeCreate(CreateView):
    model = Cube
    fields = '__all__'