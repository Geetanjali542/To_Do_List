from django.shortcuts import render
from django.http import HttpResponse
from app.models import Addtask


def index(request):
  undonetask= Addtask.objects.all().filter(is_completed = False).order_by('-updated_at')
  donetask = Addtask.objects.all().filter(is_completed = True).order_by('-updated_at')

  context = {
    'uncompletedtasks' : undonetask,
    'completedtasks' : donetask

  }
  return render(request,'todo.html', context )