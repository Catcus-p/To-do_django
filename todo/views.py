from django.shortcuts import render, redirect
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# API: list all tasks as JSON
@api_view(['GET'])
def api_task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# API: calculate completed tasks as JSON
@api_view(['GET'])
def api_calculate_completed(request):
    completed_count = Task.objects.filter(completed=True).count()
    return Response({"completed_tasks": completed_count})

# Normal page view: list tasks, add, toggle, delete
def task_list(request):
    tasks = Task.objects.all()
    completed_count = Task.objects.filter(completed=True).count()

    # Handle POST for adding new task
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('/')

    # Detect if URL is /api/calculate/ to show the calculation result
    show_calculate = request.path == '/api/calculate/'

    return render(request, 'todo/task_list.html', {
        'tasks': tasks,
        'show_calculate': show_calculate,
        'completed_count': completed_count
    })

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
