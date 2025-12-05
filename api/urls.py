from django.urls import path
from . import views

urlpatterns = [
    # Test Route
    path('hello/', views.hello, name='hello'),

    # Tasks CRUD API
    path('tasks/', views.get_tasks, name='get_tasks'),              # GET → list all tasks
    path('tasks/add/', views.create_task, name='create_task'),      # POST → create new task
    path('tasks/<int:id>/', views.update_task, name='update_task'), # PUT → update task
    path('tasks/<int:id>/delete/', views.delete_task, name='delete_task'),  # DELETE → delete task
]

