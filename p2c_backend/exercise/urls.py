from django.urls import path

from exercise.views import TaskList,TaskDetail

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
]
