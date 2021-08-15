from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from compiler.services import compile_code


class CompilerView(APIView):

    def post(self, request):
        code = request.data['code']
        output = compile_code(code)
        return Response(output, status=status.HTTP_200_OK)