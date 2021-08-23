from django.urls import path

from . import views

urlpatterns = [
    path('compiler/', views.CompilerView.as_view()),
]