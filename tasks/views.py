from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title and title.strip():
            Task.objects.create(title=title.strip())

        return redirect('home')

    tasks = Task.objects.all()

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    return render(request, 'tasks/home.html', {
    'tasks': tasks,
    'total_tasks': total_tasks,
    'completed_tasks': completed_tasks,
    'pending_tasks': pending_tasks
})


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()

    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect('home')