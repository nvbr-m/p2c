from django.urls import path

from . import views
from .views import CompilerView

urlpatterns = [
    path('compiler', views.CompilerView.as_view()),
]