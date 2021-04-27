from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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

@login_required
def cubes_index(request):
    cubes = Cube.objects.filter(user=request.user)
    return render(request, 'cubes/index.html', {'cubes': cubes})

@login_required
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

@login_required
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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

@login_required
def assoc_stand(request, cube_id, stand_id):
    Cube.objects.get(id=cube_id).stands.add(stand_id)
    return redirect('detail', cube_id=cube_id)

@login_required
def add_photo(request, cube_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        print(key)
        print(s3)
        print(S3_BASE_URL, BUCKET, 'base url and bucket')
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, cube_id=cube_id)
            print(photo)
            print(url)
            photo.save()
        except:
            print('An error occurred uploading the file to S3')
    return redirect('detail', cube_id=cube_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.us_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up, try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)