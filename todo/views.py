from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Task





def task_list(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description
        )
        return redirect('/')

    return render(request, 'todo/task_list.html', {'tasks': tasks})


def edit_task(request, id):
    task = Task.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('/')

    return render(request, 'todo/edit_task.html', {'task': task})


def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('/')


def toggle_complete(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('/')


def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)#django session create
            return redirect('/')
    return render(request, 'todo/login.html')


def user_logout(request):
   logout(request)
   return redirect('/login/')



    

# Create your views here.
