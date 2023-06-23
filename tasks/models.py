from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title: str = models.CharField('Task', max_length=255,)
    content: str = models.TextField('To do')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null = True)

    def __str__(self):
        #Повертає рядок, що представляє об'єкт Task.
       return self.title

    def get_absolute_url(self):
        #Повертає абсолютний URL-адрес для об'єкта Task.
        return f'/crate/{self.id}'

    class Meta:
        verbose_name: str = 'Task'
        verbose_name_plural: str = 'Tasks'

