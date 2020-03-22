from django.db import models


class Task(models.Model):
    task_title = models.CharField(max_length=500)
    task_description = models.TextField()
    task_creation = models.DateTimeField('Creation date')
    

    def __str__(self):
        return self.task_tile
