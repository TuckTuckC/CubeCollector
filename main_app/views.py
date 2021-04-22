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
    new_time_format = cube.time_set.all()
    print(new_time_format[0])
    return render(request, 'cubes/detail.html', {
        'cube': cube,
        'time_form': time_form
    })

def add_time(request, cube_id):
    form = TimeForm(request.POST)
    print('Add_Time')
    if form.is_valid():
        new_time = form.save(commit=False)
        new_time.cube_id = cube_id
        new_time.save()
    else:
        print(form.errors)
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

# Stands views
def stands_index(request):
    stands = stand.objects.all()
    context = {'stands': stands}
    
    return render(request, 'stand/index.html', context)


def stand_detail(request, stand_id):
    stand = stand.objects.get(id=stand_id)
    context = {
        'stand': stand
    }
    return render(request, 'stand/detail.html', context)
    
class Create_Stand(CreateView):
    model = Stand
    fields = '__all__'


class Update_stand(UpdateView):
    model = stand
    fields = ['color']

class Delete_stand(DeleteView):
    model = stand
    success_url = '/stands/' 