from django.urls import path
from . import views

urlpatterns=[
  path('addTask/',views.addTask,name='addTask'),
  path('markComplete/<int:pk>/',views.markComplete,name='markComplete'),
  path('markUncomplete/<int:pk>/',views.markUncomplete,name='markUncomplete'),
  path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
  path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
]