from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    #success_url = '/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    #success_url = '/'