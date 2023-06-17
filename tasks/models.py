from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField('Task', max_length=255,)
    content = models.TextField('To do')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null = True)

    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return f'/crate/{self.id}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

