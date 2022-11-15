from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView


class StudentView(View):
    def get(self, request):
        print(f'request={request}')

        return HttpResponse({'mse': 'ok'})


class StudentAPIView(APIView):

    def get(self, request):
        print(f'request={request}')

        return Response({'mse': 'ok'})

    def post(self, request):
        return Response({'msg': 'ok'})

    def put(self, request):
        return Response({'msg': 'ok'})

    def patch(self, request):
        return Response({'msg': 'ok'})

    def delete(self, request):
        return Response({'msg': 'ok'})
