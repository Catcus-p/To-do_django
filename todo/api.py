from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def api_task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_add_task(request):
    title = request.data.get('title')
    task = Task.objects.create(title=title)
    return Response({"message": "Task created", "id": task.id})


@api_view(['POST'])
def api_toggle_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return Response({"completed": task.completed})


@api_view(['GET'])
def api_calculate_completed(request):
    count = Task.objects.filter(completed=True).count()
    return Response({"completed_tasks": count})