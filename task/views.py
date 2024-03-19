from django.shortcuts import render, redirect
from .models import *
from datetime import datetime

def init(request):
    tasks = Task.objects.all()
    return render(
        request,
        'index.html',
        {'tasks': tasks}
    )
    
def save_task(request):
    if request.method == 'POST':
        task = Task()
        task.create_at = datetime.now()
        task.description = request.POST['task']
        task.completed = False
        task.save()
    
    return redirect('init')

def update_task(request,id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    
    return redirect('init')