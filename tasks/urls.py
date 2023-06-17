from django.urls import path
from tasks.views import *
from . import views


urlpatterns = [
    path('', base_view, name= 'main'),
    path('about', about_view, name= 'about'),
    path('crate', create_view, name= 'create'),
    path('<int:pk>',views.TaskDetailView.as_view(),name='task-detail'),
    path('<int:pk>/succed', views.TaskSuccedView.as_view(), name= 'succed-item'),
    path('<int:pk>/change', views.TaskChangeView.as_view(), name= 'change-item'),
    path('register', register, name= 'register'),
    path('login', login_view, name= 'login'),
]