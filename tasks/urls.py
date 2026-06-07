from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name = 'task-list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name = 'task-detail'),
    path('create/<int:pk>/', views.TaskCreateView.as_view(), name = 'task-create'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name = 'task-delete'),
]
