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

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title, 
            'date': task.date,
            'status': task.status,
            'description':task.description
        })
        return render(request, 'update.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.date = form.cleaned_data['date']
            task.status = form.cleaned_data['status']
            task.description = form.cleaned_data['description']
            task.save()
            return redirect('detail_task', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})