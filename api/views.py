from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


# -----------------------------
# Simple API Test Endpoint
# -----------------------------
def hello(request):
    return JsonResponse({"message": "Backend is working!"})


# -----------------------------
# GET ALL TASKS
# -----------------------------
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# -----------------------------
# CREATE NEW TASK
# -----------------------------
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# UPDATE TASK
# -----------------------------
@api_view(['PUT'])
def update_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------
# DELETE TASK
# -----------------------------
@api_view(['DELETE'])
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    task.delete()
    return Response({"message": "Deleted successfully"})


