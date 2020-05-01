from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=60, unique=True, default="New Project")
    description = models.TextField(max_length=300, default="")
    created_at = models.DateTimeField('Creation date', default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title

class TaskList(models.Model):
    title = models.CharField(max_length=60, unique=True, default="New List")
    created_at = models.DateTimeField('Creation date', default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=60, unique=True, default="New Task")
    description = models.TextField(max_length=300, default="")
    created_at = models.DateTimeField('Creation date', default=timezone.now)
    status = models.TextField("Status of task", choices=[
        ("TD", "to_do"),
        ("P", "paused"),
        ("D", "doing"),
        ("END", "done")
        ], 
        default="to_do"
    )
    task_list = models.ForeignKey(TaskList,  on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project,  on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title

