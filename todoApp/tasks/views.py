from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser
from tasks import models, serializers
from tasks import permissions as custom_permissions


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser]

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoints for tasks
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [custom_permissions.IsOwnerOrReadOnly | permissions.IsAdminUser]

class TaskListViewSet(viewsets.ModelViewSet):
    """
    API endpoints for tasks
    """
    queryset = models.TaskList.objects.all()
    serializer_class = serializers.TaskListSerializer
    permission_classes = [custom_permissions.IsOwnerOrReadOnly | permissions.IsAdminUser]

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoints for tasks
    """
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [custom_permissions.IsOwnerOrReadOnly | permissions.IsAdminUser]

    
