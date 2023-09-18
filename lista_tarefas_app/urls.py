from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registrar/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('tarefa/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('tarefa-criar/', TaskCreate.as_view(), name='task-create'),
    path('tarefa-atualizar/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('tarefa-deletar/<int:pk>/', TaskDelete.as_view(), name='task-delete')
]
