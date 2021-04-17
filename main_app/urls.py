from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cubes/', views.cubes_index, name='index'),
    path('cubes/<int:cube_id>/', views.cube_detail, name='detail'),
    path('cubes/create/', views.CubeCreate.as_view(), name='cubes_create'),
    path('cubes/<int:pk>/update/', views.CubeUpdate.as_view(), name='cubes_update'),
    path('cubes/<int:pk>/delete/', views.CubeDelete.as_view(), name='cubes_delete'),
    path('cubes/<int:cube_id>/add_time/', views.add_time, name='add_time'),
]