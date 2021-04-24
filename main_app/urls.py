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
    path('cubes/<int:cube_id/assoc_stand/<int:stand_id>/', views.assoc_stand, name='assoc_stand'),

    # stand urls
    path('stands/', views.stands_index, name='all_stands'),
    path('stands/<int:stand_id>/', views.stand_detail, name='stand_detail'),
    path('stands/create/', views.Create_stand.as_view(), name='create_stand'),
    path('stands/<int:pk>/update/', views.Update_stand.as_view(), name='update_stand'),
    path('stands/<int:pk>/delete/', views.Delete_stand.as_view(), name='delete_stand'),
]