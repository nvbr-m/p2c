from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    instruction = models.TextField()
    pascal_code = models.TextField()

    def __str__(self):
        return f'{self.id} {self.title}'


class TaskTest(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    test_case = models.CharField(max_length=50)
    expected_result = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.task} {self.test_case}'
