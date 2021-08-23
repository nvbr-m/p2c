from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from compiler.services import compile_code
from exercise.serializers import TaskSerializer, TaskDetailSerializer
from exercise.models import Task, TaskTest


class TaskList(ListAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer


class TaskDetail(APIView):

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)

    def post(self, request, pk):
        code = request.data["code"]
        test_input = self.get_test(pk)
        expected_result = self.get_expected_results(pk)
        output = compile_code(code, test_input=test_input)
        test_results = self.check_results(output, expected_result)
        return Response(test_results, status=status.HTTP_200_OK)

    def get_test(self, pk):
        return list(TaskTest.objects.filter(task__id=pk).values_list('test_case', flat=True))

    def get_expected_results(self, pk):
        return list(TaskTest.objects.filter(task__id=pk).values_list('expected_result', flat=True))

    def check_results(self, output, expected_result):
        output = list(output.values())
        passed = 0
        for value, expect in zip(output, expected_result):
            value = value.decode('utf-8')
            if value == expect:
                passed += 1
        if passed == len(expected_result):
            res = "All Tests Passed!"
        else:
            res = f"{len(expected_result) - passed} Tests Failed!"
        return {'result': f'{res}', 'passed': passed, 'total': len(expected_result)}
