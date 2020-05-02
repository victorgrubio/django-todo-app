from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=60, default="New Project")
    description = models.TextField(max_length=300, default="")
    created_at = models.DateTimeField('Creation date', default=timezone.now, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    class Meta:
        ordering = ['created_at']

class TaskList(models.Model):
    title = models.CharField(max_length=60, unique=True, default="New List")
    created_at = models.DateTimeField('Creation date', default=timezone.now, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    class Meta:
        ordering = ['created_at']


class Task(models.Model):
    title = models.CharField(max_length=60, unique=True, default="New Task")
    description = models.TextField(max_length=300, default="")
    created_at = models.DateTimeField('Creation date', default=timezone.now, editable=False)
    status = models.TextField("Status of task", choices=[
        ("TD", "to_do"),
        ("P", "paused"),
        ("D", "doing"),
        ("END", "done")
        ], 
        default="to_do"
    )
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    class Meta:
        ordering = ['created_at']
