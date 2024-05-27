from django.http import *
from django.shortcuts import render
from todos.models import *

def home(request):
  tasks = Task.objects.filter(is_completed=False).order_by('updated_at') # here we need taks that are not completed
  print(tasks)
  context={
    'tasks':tasks,
  }
  return render(request,'home.html',context)