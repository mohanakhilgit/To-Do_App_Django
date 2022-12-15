from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks': tasks})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task, 'form': form})
