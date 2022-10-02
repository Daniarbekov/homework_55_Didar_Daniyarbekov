from django.shortcuts import render, redirect
from webapp.models import Task

def index_view(request):
    if request.method == 'POST':
        to_delete_tasks = request.POST.getlist('delete')
        for del_task in to_delete_tasks:
            task=Task.objects.filter(pk=del_task)
            task.delete()
        return redirect('index')
    else :
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html',context)
    