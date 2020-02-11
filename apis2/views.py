from django.shortcuts import render
from rest_framework import generics
from task import models
from .serializers import TaskTrackerSerializer


class ListTaskTracker(generics.ListCreateAPIView):
    queryset = models.TaskTracker.objects.all()
    serializer_class = TaskTrackerSerializer


class DetailTaskTracker(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TaskTracker.objects.all()
    serializer_class = TaskTrackerSerializer
