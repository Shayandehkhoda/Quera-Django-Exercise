from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.http import HttpResponse

@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        task = Task(name=task_name)
        task.save()
        return HttpResponse(f"Task Created: '{task.name}'")