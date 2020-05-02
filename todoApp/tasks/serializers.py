from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tasks import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.Task
        fields = ['id', 'title', 'description', 'owner', 'created_at', 'status', 'task_list', 'project']

class TaskListSerializer(serializers.ModelSerializer):
    
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.TaskList
        fields = ['id', 'title', 'owner', 'created_at', 'project']

class ProjectSerializer(serializers.ModelSerializer):
    
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.Project
        fields = ['id', 'title', 'description', 'owner', 'created_at']