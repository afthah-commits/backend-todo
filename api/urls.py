from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('tasks/', views.get_tasks),
    path('tasks/add/', views.create_task),
    path('tasks/<int:id>/', views.update_task),
    path('tasks/<int:id>/delete/', views.delete_task),
]
