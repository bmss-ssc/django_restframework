import json

from django.http import JsonResponse
from django.views import View
from .models import Student


class StudentView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        sex = data.get('sex')
        age = data.get('age')
        classmate = data.get('classmate')
        description = data.get('description')

        instance = Student.objects.create(
            name=name,
            sex=sex,
            age=age,
            classmate=classmate,
            description=description,
        )

        return JsonResponse(data={
            'id': instance.pk,
            'name': instance.name,
            'sex': instance.sex,
            'age': instance.age,
            'classmate': instance.classmate,
            'description': instance.description,
        }, status=201)

    def get(self, request):
        student_list = list(Student.objects.values())

        return JsonResponse(data=student_list, status=200, safe=False)


class StudentInfo(View):
    def get(self, request, pk):

        try:
            instance = Student.objects.get(pk=pk)
            return JsonResponse(data={
                'id': instance.pk,
                'name': instance.name,
                'sex': instance.sex,
                'age': instance.age,
                'classmate': instance.classmate,
                'description': instance.description,
            }, status=200)

        except Student.DoesNotExist:
            return JsonResponse(data={}, status=204)

    def put(self, request, pk):
        data = json.loads(request.body)
        print(f'data={data}')
        name = data.get('name')
        sex = data.get('sex')
        age = data.get('age')
        classmate = data.get('classmate')
        description = data.get('description')
        try:
            instance = Student.objects.get(pk=pk)
            instance.name = name
            instance.sex = sex
            instance.age = age
            instance.classmate = classmate
            instance.description = description
            instance.save()
            return JsonResponse(data={
                'id': instance.pk,
                'name': instance.name,
                'sex': instance.sex,
                'age': instance.age,
                'classmate': instance.classmate,
                'description': instance.description,
            }, status=200)

        except Student.DoesNotExist:
            return JsonResponse(data={}, status=204)

    def delete(self, request, pk):
        try:
            Student.objects.filter(pk=pk).delete()
            return JsonResponse(data={}, status=204)

        except Student.DoesNotExist:
            return JsonResponse(data={}, status=204)
