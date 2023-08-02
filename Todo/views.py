from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def main(request):
    tasks = Task.objects.all()
    return render(request, 'main.html',{'tasks':tasks})

def item(request,id):
    task = Task.objects.get(id=id)
    return HttpResponse(task.name)
    # return render(request, 'item.html',{'task':task})