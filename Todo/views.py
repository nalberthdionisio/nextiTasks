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
    # return HttpResponse(task.name)
    print(task)
    return render(request, 'item.html',{'task':task, 'tasks':tasks})

def formtasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    return render(request, 'formtasks.html', {'form': form})

def taskdelete(request,id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("/main")

    