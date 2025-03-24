from django.shortcuts import render
from todolistapp.models import Task, Taskers
from rest_framework import generics
from .serializers import TaskersSerializer, TaskSerializer


# Create your views here.
#CRUD operations for the tasker
class TaskerListCreate(generics.ListCreateAPIView):
    queryset = Taskers.objects.all()
    serializer_class = TaskersSerializer

class TaskerRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taskers.objects.all()
    serializer_class = TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer