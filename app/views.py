from django.shortcuts import get_object_or_404, render, redirect
from app.models import Addtask

# Create your views here.
def todoadd(request):
  if request.method == 'POST':
    newtask = request.POST.get('addtask')
    Addtask.objects.create(addtask = newtask)
    return redirect('index')
  # return render(request, 'todo.html')

def tododelete(request, pk):
  objDelete = get_object_or_404(Addtask, pk = pk)
  objDelete.delete()
  return redirect('index')

def todoedit(request, pk):
  objEdit = get_object_or_404(Addtask, pk = pk)
  if request.method == 'POST':
    edit = request.POST.get('addtask') #we can't directly save the modified task because if we do then if we save the details without changing them it will say an error
    objEdit.addtask = edit
    objEdit.save()
    return redirect('index')
  else:
    context = {
      'objEdit' : objEdit,
    }
    return render(request, 'edit.html', context)
  

def taskdone(request, pk):
  taskdone = get_object_or_404(Addtask, pk=pk)
  taskdone.is_completed = True
  taskdone.save()
  return redirect('index')

def taskundone(request, pk):
  taskundone = get_object_or_404(Addtask, pk=pk)
  taskundone.is_completed = False
  taskundone.save()
  return redirect('index')