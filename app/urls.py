from django.urls import path
from . import  views

urlpatterns = [
  path('todoadd', views.todoadd, name='todoadd'),
  path('tododelete/<int:pk>/', views.tododelete, name='tododelete'),
  path('todoedit/<int:pk>/', views.todoedit, name='todoedit'),  
  path('taskdone/<int:pk>/', views.taskdone, name='taskdone'),
  path('taskundone/<int:pk>/', views.taskundone, name='taskundone'),
]
