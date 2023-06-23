from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    list_filter = ('user',)
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'user')

admin.site.register(Task, TaskAdmin)

