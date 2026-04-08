from django.shortcuts import render,redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('/')

    return render(request, 'todo/task_list.html', {'tasks': tasks})
    
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def toggle_complete(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('/')


    

# Create your views here.
