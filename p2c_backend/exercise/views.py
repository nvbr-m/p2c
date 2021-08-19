from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from exercise.serializers import TaskSerializer, TaskDetailSerializer
from exercise.models import Task


class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)
