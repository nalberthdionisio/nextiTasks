from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from .models import *
from .forms import *
# Create your views here.
def main(request):
    tasks = Task.objects.all()
    return render(request, 'main.html',{'tasks':tasks})

def item(request, id):
    tasks = Task.objects.all()

    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        print(form.errors)
        if form.is_valid():
            form.save()

    return render(request, 'item.html',{'task':task, 'tasks':tasks, 'form':form})

def formtasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/main")
    else:
        form = TaskForm()
    return render(request, 'formtasks.html', {'form': form})

def taskdelete(request,id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("/main")

def taskedit(request,id):
    pass