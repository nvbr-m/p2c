from django.contrib import admin

# Register your models here.
from exercise.models import Task, TaskTest


class TestInline(admin.TabularInline):
    model = TaskTest

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [
        TestInline,
    ]



