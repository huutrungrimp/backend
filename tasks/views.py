from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from accounts.models import User
from customers.models import Customer
from .serializers import TaskSerializer
from rest_framework import status


@api_view(['PUT'])
def updateTask(request, username, id):
    try:
        task = Task.objects.get(id=id)        
        
    except Task.DoesNotExist:
        return Response({"error": "The task is not found"}, status=404)

    if request.method == "GET":
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'You do not have permision.'})


@api_view(['DELETE'])
def deleteTask(request, username, id):
    task = Task.objects.get(id=id)
    task.delete()

    return Response({'message': 'task was deleted'})


@api_view(['GET'])
def taskDetail(request, username, id):
    task = Task.objects.get(id=id)
    serializers = TaskSerializer(task, many=False)

    return Response(serializers.data)


@api_view(['GET'])
def taskList(request, username):
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks, many=True)

    return Response(serializers.data)


@api_view(['POST'])
def createTask(request, username, customerID):
    if request.method != "POST":
        return Response({"error": "Task request required."})

    user = User.objects.get(username=username)
    title = request.data["title"]
    date_time_start = request.data['date_time_start']
    date_time_end = request.data['date_time_end']
    hours = request.data['hours']
    customer = Customer.objects.get(id=customerID)

    task = Task.objects.create(
        user = user,
        title = title,
        date_time_start = date_time_start,
        date_time_end = date_time_end,
        hours = hours,
        customer = customer,
    )
    task.save()

    return Response(TaskSerializer(task).data)