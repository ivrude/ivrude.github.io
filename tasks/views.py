from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, DetailView, UpdateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'tasks/register.html', {'error': 'User already exists'})

        return redirect('login')

    return render(request, 'tasks/register.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Додайте додаткову логіку, якщо потрібно
            return redirect('main')  # Перенаправлення на сторінку після входу
        else:
            return render(request, 'tasks/login.html', {'error': 'Invalid credentials'})
    return render(request, 'tasks/login.html')
class TaskSuccedView(DeleteView):
    model=Task
    template_name = 'tasks/delete.html'
    success_url = '/'

class TaskDetailView(DetailView):
    model=Task
    template_name = 'tasks/details_view.html'
    context_object_name= 'article'

class TaskChangeView(UpdateView):
    model=Task
    template_name = 'tasks/change.html'
    context_object_name= 'article'
    success_url = '/'
    form_class = TaskForm

def base_view(request):
    current_user = request.user.id
    tasks = Task.objects.all().filter(user=current_user)
    return render(request, 'profile/index.html', {'title': 'Main Page','tasks': tasks })

def about_view(request):
    return render(request, 'tasks/main.html',)



def create_view(request):
    error = ''
    try:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect('main')
    except Exception as e:
        return redirect('register')
    form = TaskForm()
    dict={
        'form': form,
        'error': error
    }
    return render(request, 'tasks/create.html',dict)


