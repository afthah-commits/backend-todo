from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    
    # Task CRUD API
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('tasks/add/', views.create_task, name='create_task'),
    path('tasks/<int:id>/', views.update_task, name='update_task'),
    path('tasks/<int:id>/delete/', views.delete_task, name='delete_task'),
]
