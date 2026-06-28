from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TaskFilterForm
from .models import Task
from .forms import TaskForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status")
        priority = self.request.GET.get("priority")

        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task-list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task-list')

class CustomLogoutView(LogoutView):
    next_page = 'tasks:task-list'

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy('tasks:task-list'))

