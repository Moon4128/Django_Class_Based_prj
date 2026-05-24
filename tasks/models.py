from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS_CHOISES = (
        ('todo','To Do'),
        ('in_progress','In Progress'),
        ('done','Done'),
    )

    PRIORITY_CHOISES = (
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOISES, default='low')
    deadline = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')


    def __str__(self):
        return self.title