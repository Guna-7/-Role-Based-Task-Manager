from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from rest_framework import permissions
from .serializers import TaskSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.userprofile.role == 'manager':
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.userprofile.role == 'manager':
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.userprofile.role != 'manager':
            return Response({"detail": "Only managers can create tasks."},
                            status=status.HTTP_403_FORBIDDEN)

        return super().create(request, *args, **kwargs)
