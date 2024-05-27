from django.http import *
from django.shortcuts import render
from todos.models import *

def home(request):
  tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') # here we need taks that are not completed
  completed_tasks=Task.objects.filter(is_completed=True)

  context={
    'tasks':tasks,
    'completed_tasks':completed_tasks
  }
  return render(request,'home.html',context)