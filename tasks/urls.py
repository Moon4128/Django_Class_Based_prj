from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name = 'task-list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name = 'task-detail'),
    path('create/', views.TaskCreateView.as_view(), name = 'task-create'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name = 'task-delete'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name = 'task-update'),
    path('Logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('Login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
]
