from django.shortcuts import render

from django.http import HttpResponse


class Cube:
    def __init__(self, name, brand, description):
        self.name = name
        self.brand = brand
        self.description = description

cubes = [
    Cube('365 Air M', 'GAN', 'Very light cube with magnets'),
    Cube('ThunderClap', 'MoFangGe', 'Best speed cube for the price'),
    Cube('Pyraminx', 'MoYu', 'Best pyraminx on the market with magnets'),
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cubes_index(request):
    return render(request, 'cubes/index.html', {'cubes': cubes})