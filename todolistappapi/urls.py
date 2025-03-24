from django.urls import path
from.views import (TaskerListCreate, TaskerRetrieveUpdateDelete, TaskListCreate
                   , TaskRetrieveUpdateDelete)

urlpatterns = [
    #taskers CRUD
    path('taskers/', TaskerListCreate.as_view(), name='tasker-list-create'),
    path('tasker/<int:pk>/', TaskRetrieveUpdateDelete.as_view(), name='tasker-retrieve-update-delete'),
    #tasks CRUD
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDelete.as_view(), name='task-retrieve-update-delete'),
]