from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializers

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = TaskSerializers