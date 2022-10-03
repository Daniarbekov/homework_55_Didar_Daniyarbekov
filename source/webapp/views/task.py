from webapp.models import Task
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import TaskForm


def task_create_view(request, *args, **kwargs):
    form = TaskForm()
    if request.method == 'GET':
        return render(request, 'task_create.html', context={'form': form})
    form = TaskForm(request.POST)
    if not form.is_valid():    
        return render(request, 'task_create.html', context={'form': form})
    task = Task.objects.create(**form.cleaned_data)        
    if request.method =='POST':
        return redirect('detail_task', pk=task.pk)

def detail_view(request,pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail_task.html', context={'task': task})