from curses.ascii import HT
from django.http import HttpResponse
from .models import Task


def list_create_tasks(request):
    if request.method == 'GET':
        task_list = Task.objects.values_list('name', flat=True).order_by('name')
        return HttpResponse('<br>'.join(map(str, task_list)))



def count_tasks(request):
    if request.method == 'GET':
        task_count = Task.objects.count()
        return HttpResponse(f"You have '{task_count}' tasks to do")
