from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, DetailView, UpdateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def register(request):
    """
       New user registration.

       :param request: the request object
       :return: the response object
       """
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
    """
      User login.

      :param request: the request object
      :return: the response object
      """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')  # Перенаправлення на сторінку після входу
        else:
            return render(request, 'tasks/login.html', {'error': 'Invalid credentials'})
    return render(request, 'tasks/login.html')
class TaskSuccedView(DeleteView):
    """
    View to delete a task.

     :param model: Task model
     :param template_name: The template to display
     :param success_url: URL after successful uninstallation
     """
    model=Task
    template_name = 'tasks/delete.html'
    success_url = '/'

class TaskDetailView(DetailView):
    """
    View for a detailed view of the task.

    :param model: Task model
    :param template_name: The template to display
    :param context_object_name: the name of the context variable
    """
    model=Task
    template_name = 'tasks/details_view.html'
    context_object_name= 'article'

class TaskChangeView(UpdateView):
    """
    Presentation to change the task.

    :param model: Task model
    :param template_name: The template to display
    :param context_object_name: the name of the context variable
    :param success_url: URL after successful update
    :param form_class: the class of the form
    """
    model=Task
    template_name = 'tasks/change.html'
    context_object_name= 'article'
    success_url = '/'
    form_class = TaskForm

def base_view(request):
    """
        Presentation of the main page.

        :param request: the request object
        :return: the response object
        """
    current_user = request.user.id
    tasks = Task.objects.all().filter(user=current_user)
    return render(request, 'profile/indexx.html', {'title': 'Main Page','tasks': tasks })

def about_view(request):
    """
      Introducing the "About Us" page.

      :param request: the request object
      :return: the response object
      """
    return render(request, 'tasks/main.html',)



def create_view(request):
    """
    Introducing creating a new task.

    :param request: the request object
    :return: the response object
    """
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


