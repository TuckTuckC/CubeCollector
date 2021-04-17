from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cubes/', views.cubes_index, name='index'),
    path('cubes/<int:cube_id>/', views.cube_deatils, name='deatils')
]