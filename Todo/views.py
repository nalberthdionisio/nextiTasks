from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
@login_required(login_url='/login')
def main(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data.update({'user': request.user})
        form = TaskForm(post_data)
        if form.is_valid():
            form.save()
            return redirect("/")
            # return redirect("/main")
    else:
        form = TaskForm()
    return render(request, 'main.html',{'tasks':tasks,'form': form})
  
@login_required(login_url='/login')
def item(request, id):
    tasks = Task.objects.all()

    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data.update({'user': request.user})
        form = TaskForm(post_data, instance=task)
        print(form.errors)
        if form.is_valid():
            form.save()

    return render(request, 'item.html',{'task':task, 'tasks':tasks, 'form':form})

@login_required(login_url='/login')
def formtasks(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data.update({'user': request.user})
        form = TaskForm(post_data)
        if form.is_valid():
            form.save()
            return redirect("/")
            # return redirect("/main")
    else:
        form = TaskForm()
    return render(request, 'formtasks.html', {'form': form, 'tasks':tasks})
  
@login_required(login_url='/login')
def taskdelete(request,id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("/")

@login_required(login_url='/login')
def taskedit(request,id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("/")