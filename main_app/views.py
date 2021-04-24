from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cube, Stand, Photo
from .forms import TimeForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-1.amazonaws.com/'
BUCKET = 'tuckercubecollector'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cubes_index(request):
    cubes = Cube.objects.all()
    return render(request, 'cubes/index.html', {'cubes': cubes})

def cube_detail(request, cube_id):
    cube = Cube.objects.get(id=cube_id)

    stands_cube_doesnt_have = Stand.objects.exclude(id__in = cube.stands.all().values_list('id'))
    time_form = TimeForm()
    new_time_format = cube.time_set.all()
    return render(request, 'cubes/detail.html', {
    'cube': cube, 
    'time_form': time_form,
    # Add the stands to be displayed
    'stands': stands_cube_doesnt_have
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
    stands = Stand.objects.all()
    context = {'stands': stands}
    
    return render(request, 'stand/index.html', context)


def stand_detail(request, stand_id):
    stand = Stand.objects.get(id=stand_id)
    context = {
        'stand': stand
    }
    return render(request, 'stand/detail.html', context)
    
class Create_stand(CreateView):
    model = Stand
    fields = '__all__'


class Update_stand(UpdateView):
    model = Stand
    fields = ['color']

class Delete_stand(DeleteView):
    model = Stand
    success_url = '/stands/' 

def assoc_stand(request, cube_id, stand_id):
    Cube.objects.get(id=cube_id).stands.add(stand_id)
    return redirect('detail', cube_id=cube_id)