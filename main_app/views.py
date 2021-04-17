from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cube
from .forms import TimeForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cubes_index(request):
    cubes = Cube.objects.all()
    return render(request, 'cubes/index.html', {'cubes': cubes})

def cube_detail(request, cube_id):
    cube = Cube.objects.get(id=cube_id)
    time_form = TimeForm()
    return render(request, 'cubes/detail.html', {
        'cube': cube,
        'time_form': time_form
    })

def add_time(request, cube_id):
    form = TimeForm(request.POST)

    if form.is_valid():
        new_time = form.save(commit=False)
        new_time.cube_id = cat_id
        new_time.save()
    return redirect('detail', cube_id=cube_id)

class CubeCreate(CreateView):
    model = Cube
    fields = '__all__'

class CubeUpdate(UpdateView):
    model = Cube
    fields = ['description']

class CubeDelete(DeleteView):
    model = Cube
    success_url = '/cubes/'