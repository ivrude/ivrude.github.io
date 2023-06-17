from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Task

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'content',]
        exclude = ['user',]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input name of the task'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input what to do'
            }),
        }
